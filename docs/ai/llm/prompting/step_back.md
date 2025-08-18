# Step-Back

## Description

Step-back prompting is a technique designed to improve LLM performance by encouraging a broader, more general reasoning step before addressing a specific task.
It works by asking a general question first, capturing the LLM's broader knowledge, and then using that response as context for the specific prompt.

This activates background reasoning processes that often remain unused in direct prompting.

## Benefits

- **Improved accuracy and insight**: Encourages critical thinking and novel knowledge application.
- **Bias mitigation**: Reduces reliance on biased, narrow interpretations by generalizing first.
- **Utilizes latent knowledge**: Unlocks parameters and reasoning paths not accessed through direct prompts.

## Example

**Prompt (general question):**

> Based on popular first-person shooter action games, what are 5 fictional key settings that contribute to a challenging and engaging level storyline in a first-person shooter video game?

**Output:**

1. **Abandoned Military Base**
2. **Cyberpunk City**
3. **Alien Spaceship**
4. **Zombie-Infested Town**
5. **Underwater Research Facility**

**Prompt (primary prompt):**

> 1. Abandoned Military Base
> 2. Cyberpunk City
> 3. Alien Spaceship
> 4. Zombie-Infested Town
> 5. Underwater Research Facility
>
> Take one of the themes and write a one-paragraph storyline for a new level of a first-person shooter video game that is challenging and engaging.

**Output:**

A richly detailed, atmospheric narrative centered on the **Underwater Research Facility**, involving mutated sea creatures, malfunctioning tech, and intense underwater survival elements, showcasing a deeper and more immersive response.
