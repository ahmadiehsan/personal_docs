# ReAct {ReWOO}

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

## Varieties

=== "Standard"

    ReAct operates through a cyclical "think-act-observe" pattern, where an AI engages in reasoning, performs an action, examines the resulting feedback, and then adjusts its subsequent actions accordingly, facilitating a dynamic and responsive problem-solving strategy.

=== "ReWOO"

    Reasoning WithOut Observation (ReWOO), is a framework that combines a multi-step planner and variable substitution for effective tool use.
    It aims to improve upon ReAct-style agents by **reducing token consumption and execution time by generating the full chain of tool usage in a single pass**, thus minimizing redundant LLM calls.

    ReWOO emphasizes comprehensive **upfront planning, generating a complete sequence of actions before any execution occurs**, thereby minimizing the necessity for continuous observation and feedback.

    So, ReWOO refers to an LLM's ability to make inferences, predictions, or decisions about scenarios it has not directly observed or been trained on.
    ReWOO enhances this by incorporating external tool use into the reasoning process.

    Advantages:

    - **Reduced token consumption and execution time**: By generating the entire plan in a single pass and using variable substitution, ReWOO minimizes redundant LLM calls and context passing
    - **Simplified fine-tuning**: The independence of the planning data from tool outputs (in theory) allows for fine-tuning without the need to invoke the tools
    - **Efficient LLM calls**: The LLM tool receives less of the prompt, making calls more token-efficient compared to the ReACT paradigm

## Use Cases

=== "Standard"

    - **Complex Question Answering**: Solves questions that require multiple reasoning steps and external lookups, such as answering open-domain questions using both knowledge and real-time data.
    - **Tool-Augmented Reasoning**: Integrates calculators, search engines, or databases to enhance the model's capabilities beyond its training data.
    - **Interactive Agents**: Powers chatbots and virtual assistants that need to reason, plan, and act in real time to fulfill user requests.

=== "ReWOO"

    ReWOO’s ability to plan and reason without direct observation makes it suitable for complex planning and decision-making tasks:

    - **Strategic Planning**: As mentioned, ReWOO can generate strategic plans based on hypothetical situations, goals, and constraints
    - **Scenario Analysis**: ReWOO can explore multiple potential outcomes of a given scenario, considering various factors and uncertainties
    - **Resource Allocation**: By planning tool use and reasoning about their results, ReWOO can optimize resource allocation in complex environments
    - **Risk Assessment**: ReWOO can help assess potential risks and develop mitigation strategies by simulating different scenarios and their consequences

## Workflow

=== "Standard"

    The chain operates in a sequence of steps where the model evaluates a query, determines the necessary actions, and executes these actions while continuing to reason about the information being processed.

    Key components of the ReAct chain include:

    - **Actionable Reasoning**: The model not only thinks about the answer but also considers how to obtain information or perform actions that lead to the answer.
    - **Interleaved Processing**: Reasoning and acting are not separate phases; instead, they occur in tandem, with the model constantly evaluating the best course of action.
    - **Feedback Loops**: The model can refine its actions based on the outcomes of previous actions, allowing for dynamic adjustment of strategies.

    This chain is particularly powerful in scenarios where information is constantly changing or where the model's built-in knowledge is insufficient to answer a query comprehensively.

=== "ReWOO"

    The ReWOO architecture consists of three modules:

    - **Planner**: Generates a high-level plan to solve the problem, including identifying which tools to use and their arguments, potentially using **variable substitution** to represent dependencies between steps. Variable substitution in AI planning, particularly within systems such as ReWOO, enables the creation of flexible and efficient plans by employing placeholders to represent values that are determined during execution. This technique allows the AI to define dependencies between steps, such as using the output of a search tool as the input for a price extraction tool, without needing to know the specific values in advance. By using variables such as `search_result` or `price`, the AI can construct a clear blueprint of the task, deferring the resolution of dynamic information until it becomes available, thereby streamlining the planning process and avoiding unnecessary computations.
    - **Worker**: Executes the tool with the provided arguments, potentially using variable substitution from previous steps.
    - **Solver**: Generates the final answer based on the tool observations and the plan.

## Example

=== "Standard"

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

=== "ReWOO"

    ```python
    import re
    from typing import List
    from typing_extensions import TypedDict
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_community.tools.tavily_search import TavilySearchResults
    from langgraph.graph import END, StateGraph, START

    # 1. Define state
    class ReWOO(TypedDict):
        task: str
        plan_string: str
        steps: List
        results: dict
        result: str

    # 2. Planner prompt and logic
    model = ChatOpenAI(model="gpt-4o")

    prompt = """For the following task, create a series of plans that can solve the problem step-by-step.
    For each plan, specify which external tool and its corresponding input should be used to gather evidence.
    You can store the evidence in a variable #E (e.g., #E1, #E2, #E3, etc.) that can be referenced by subsequent tools.
    Note that all the variables are independent, so make sure to include all necessary information in each tool input.

    Tools can be one of the following:

    Google[input]: A search engine worker that retrieves results from Google.
    Use this when you need concise answers or information about a specific topic.
    The input should be a search query.

    LLM[input]: A pretrained Large Language Model (like me).
    Use this when you need to leverage general world knowledge, common sense, or perform complex reasoning.
    Prioritize this tool when you are confident in solving the problem without external assistance.
    The input can be any instruction or question.

    Calculator[input]: A tool that can perform mathematical calculations.
    Use this when you need to perform arithmetic operations.
    The input should be a valid mathematical expression.

    WolframAlpha[input]: A computational knowledge engine.
    Use this when you need to solve equations, perform symbolic calculations, or get data-driven answers.
    The input should be a query in Wolfram Language or natural language related to a math or science problem.

    For example,

    Task: Alice, Bob, and Carol earned a total of $540 from their part-time jobs last week.
    Alice earned y dollars.
    Bob earned $20 more than three times what Alice earned, and Carol earned $15 more than Bob.
    How much money did Carol earn?

    Plan: Given Alice earned y dollars, translate the problem into algebraic expressions and solve with Wolfram Alpha.
    #E1 = WolframAlpha[Solve y + (3y + 20) + ((3y + 20) + 15) = 540]

    Plan: Find out the amount of money Alice earned.
    #E2 = LLM[What is y, given #E1]

    Plan: Calculate the amount of money Carol earned.
    #E3 = Calculator[((3 * #E2) + 20) + 15]

    Begin!
    Describe your plans with rich details.
    Each Plan should be followed by only one #E.

    Task: {task}"""

    # 3. Node for planner
    regex_pattern = r"Plan:\s*(.+)\s*(#E\d+)\s*=\s*(\w+)\s*\[([^\]]+)\]"
    prompt_template = ChatPromptTemplate.from_messages([("user", prompt)])
    planner = prompt_template | model

    def get_plan(state: ReWOO):
        task = state["task"]
        result = planner.invoke({"task": task})
        matches = re.findall(regex_pattern, result.content)
        return {"steps": matches, "plan_string": result.content}

    # 4. Define the tool execution logic
    search = TavilySearchResults()

    def _get_current_task(state: ReWOO):
        if "results" not in state or state["results"] is None:
            return 1
        if len(state["results"]) == len(state["steps"]):
            return None
        else:
            return len(state["results"]) + 1

    def tool_execution(state: ReWOO):
        _step = _get_current_task(state)
        _, step_name, tool, tool_input = state["steps"][_step - 1]
        _results = (state["results"] or {}) if "results" in state else {}

        for k, v in _results.items():
            tool_input = tool_input.replace(k, v)

        if tool == "Google":
            result = search.invoke(tool_input)
        elif tool == "LLM":
            result = model.invoke(tool_input)
        else:
            raise ValueError

        _results[step_name] = str(result)
        return {"results": _results}

    # 5. Solver prompt and logic
    solve_prompt = """Solve the following task or problem.
    To solve the problem, we have made step-by-step Plan and retrieved corresponding Evidence to each Plan.
    Use them with caution since long evidence might contain irrelevant information.

    {plan}

    Now solve the question or task according to provided Evidence above.
    Respond with the answer directly with no extra words.

    Task: {task}
    Response:"""

    def solve(state: ReWOO):
        plan = ""

        for _plan, step_name, tool, tool_input in state["steps"]:
            _results = (state["results"] or {}) if "results" in state else {}

            for k, v in _results.items():
                tool_input = tool_input.replace(k, v)
                step_name = step_name.replace(k, v)

            plan += f"Plan: {_plan}\n{step_name} = {tool}[{tool_input}]\n"

        prompt = solve_prompt.format(plan=plan, task=state["task"])
        result = model.invoke(prompt)
        return {"result": result.content}

    # 6. Build workflow
    def _route(state):
        _step = _get_current_task(state)
        if _step is None:
            return "solve"
        else:
            return "tool"

    graph = StateGraph(ReWOO)
    graph.add_node("plan", get_plan)
    graph.add_node("tool", tool_execution)
    graph.add_node("solve", solve)
    graph.add_edge("plan", "tool")
    graph.add_edge("solve", END)
    graph.add_conditional_edges("tool", _route)
    graph.add_edge(START, "plan")

    app = graph.compile()

    # 7. Execution
    task = "what is the exact hometown of the 2024 mens australian open winner"
    for s in app.stream({"task": task}):
        print(s)
        print("---")
    ```

    !!! info

        The `_route` function acts as a conditional director, determining the next step based on the current state.
        It checks if further tool-based actions are required; if not, it routes the process to the "solve" node for final answer generation.
        Otherwise, it directs it to the "tool" node for tool execution.
