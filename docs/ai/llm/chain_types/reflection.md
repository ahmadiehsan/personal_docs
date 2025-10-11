# Reflection

## Description

Reflection in LLMs refers to a model's ability to analyze, evaluate, and improve its own outputs.
This meta-cognitive capability allows LLMs to engage in iterative refinement, potentially leading to higher- quality results and more robust performance.

There are several key aspects of reflection:

- Self-evaluation of outputs
- Identification of weaknesses or errors
- Generation of improvement strategies
- Iterative refinement of responses

## Varieties

=== "Self-Evaluation"

    Self-evaluation involves the model critically assessing its own output to identify strengths, weaknesses, and areas for improvement before suggesting enhancements.

=== "Iterative Refinement"

    Iterative refinement is a process where a model's response is **progressively improved through repeated cycles of self-evaluation and revision**.
    Each cycle uses a reflection prompt to guide the model in critiquing and enhancing its prior output, aiming to converge on a more accurate or well-articulated result.

=== "Error Correction"

    Error correction focuses on identifying and fixing specific mistakes in the model's output, often guided by known errors or external feedback.

## Example

=== "Self-Evaluation"

    ```python
    def self_evaluation_prompt(task, initial_response):
        prompt = f"""Task: {task}

        Initial Response:
        {initial_response}

        Now, let's engage in self-reflection:

        1. Evaluate the strengths and weaknesses of your initial response.
        2. Identify any errors, inconsistencies, or areas for improvement.
        3. Suggest specific ways to enhance the response.
        4. Provide a revised and improved version of the response.

        Your self-reflection and improved response:
        """
        return prompt

    task = "Explain the concept of quantum entanglement to a high school student."
    initial_response = "Quantum entanglement is when two particles are connected in a way that measuring one instantly affects the other, no matter how far apart they are."
    prompt = self_evaluation_prompt(task, initial_response)
    print(prompt)
    ```

=== "Iterative Refinement"

    ```python
    def iterative_reflection(model, tokenizer, task, max_iterations=3):
        response = generate_initial_response(model, tokenizer, task)

        for _ in range(max_iterations):
            prompt = self_evaluation_prompt(task, response)
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(inputs, max_length=1000, num_return_sequences=1)
            reflection = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract the improved response from the reflection
            response = extract_improved_response(reflection)

            if is_satisfactory(response):
                break

        return response

    def generate_initial_response(model, tokenizer, task):
        prompt = f"Task: {task}\n\nResponse:"
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=500, num_return_sequences=1)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    def extract_improved_response(reflection):
        # Implement logic to extract the improved response from the reflection
        # This could involve text parsing or using markers in the generated text
        pass

    def is_satisfactory(response):
        # Implement logic to determine if the response meets quality criteria
        # This could involve length checks, keyword presence, or more advanced metrics
        pass
    ```

=== "Error Correction"

    ```python
    def error_correction_reflection(model, tokenizer, task, initial_response, known_errors):
        prompt = f"""Task: {task}

        Initial Response:
        {initial_response}

        Known Errors:
        {' '.join(f'- {error}' for error in known_errors)}

        Please reflect on the initial response, focusing on correcting the known errors.
        Provide an improved version of the response that addresses these issues.

        Corrected Response:
        """

        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=1000, num_return_sequences=1)
        corrected_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return corrected_response

    task = "Describe the structure of an atom."
    initial_response = "An atom consists of a nucleus containing protons and neutrons, with electrons orbiting around it in fixed circular orbits."
    known_errors = [
        "Electrons do not orbit in fixed circular paths",
        "The description doesn't mention electron shells or energy levels"
    ]

    corrected_response = error_correction_reflection(model, tokenizer, task, initial_response, known_errors)
    print(corrected_response)
    ```
