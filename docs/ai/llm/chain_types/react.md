# ReAct

## Description

The ReAct (Reasoning and Acting) chain enables language models to interleave reasoning steps with actions, such as querying external tools or databases.
This approach allows the model to dynamically decide when to think, when to act, and how to combine information from multiple sources to answer complex queries.

Advantages:

- **Dynamic tool use**: Integrates reasoning with external actions, allowing the model to fetch up-to-date or specialized information as needed.
- **Improved problem-solving**: Enables step-by-step reasoning, making it suitable for tasks that require multi-hop logic or intermediate calculations.
- **Transparency**: The reasoning process is explicit, making it easier to trace how answers are derived.

Disadvantages:

- **Increased latency**: Each action (e.g., external API call) adds to the response time.
- **Complexity in orchestration**: Requires careful design to manage the sequence of reasoning and actions.
- **Dependency on external tools**: The quality of results depends on the reliability and accuracy of the integrated tools.

## Use Cases

- **Complex Question Answering**: Solves questions that require multiple reasoning steps and external lookups, such as answering open-domain questions using both knowledge and real-time data.
- **Tool-Augmented Reasoning**: Integrates calculators, search engines, or databases to enhance the model's capabilities beyond its training data.
- **Interactive Agents**: Powers chatbots and virtual assistants that need to reason, plan, and act in real time to fulfill user requests.

## Workflow

The chain operates in a sequence of steps where the model evaluates a query, determines the necessary actions, and executes these actions while continuing to reason about the information being processed.

Key components of the ReAct chain include:

- **Actionable Reasoning**: The model not only thinks about the answer but also considers how to obtain information or perform actions that lead to the answer.
- **Interleaved Processing**: Reasoning and acting are not separate phases; instead, they occur in tandem, with the model constantly evaluating the best course of action.
- **Feedback Loops**: The model can refine its actions based on the outcomes of previous actions, allowing for dynamic adjustment of strategies.

This chain is particularly powerful in scenarios where information is constantly changing or where the model's built-in knowledge is insufficient to answer a query comprehensively.

## Example

```python
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain
from langchain.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

# 1. Define Tools: In this simple example, we are using a search tool.
tools = [DuckDuckGoSearchRun()]

# 2. Construct the Prompt:
template = """Answer the following questions as best you can. You have
access to the following tools:

{tool_descriptions}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
{agent_scratchpad}"""

prompt = ChatPromptTemplate.from_template(template)
prompt = prompt.partial(
    tool_names=", ".join([t.name for t in tools]),
    tool_descriptions="\n".join([f"{t.name}: {t.description}" for t in tools]),
)

# 3. Instantiate the LLM:
llm = ChatOpenAI(temperature=0)
llm_with_stop = llm.bind(stop=["\nObservation:"])  # Configure it to stop when it sees '\nObservation:'

# 4. Construct the Agent Pipeline:
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),
    }
    | prompt
    | llm_with_stop
    | ReActSingleInputOutputParser()
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

sample_question = "Who is the current CEO of Microsoft and what is their age squared?"
response = agent_executor.invoke({"input": sample_question})
print(response)
```

!!! info

    Agent Execution Process:

    1. We create an `AgentExecutor` instance
    2. The `agent_executor.invoke` method starts the process.
    3. Then, `AgentExecutor` manages the ReAct loop:

       1. It feeds the input to the agent pipeline.
       2. The agent (LLM and parser) decides on an action (for example, using a search tool to find the CEO's name).
       3. The `AgentExecutor` executes the action (calls the search tool).
       4. It passes the result back to the agent as an "Observation."
       5. This process repeats until the agent decides it has enough information to produce a final answer.
