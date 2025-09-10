# Code Review Guide

## Review Process

### Big Picture

- Consider how the change fits into the overall system and architecture.
- Check for updates to related code, documentation, and tests.
- Ask: Does this impact future work or introduce risks?
- Review all call-sites and ensure consistency across the codebase.

### Naming

- Prioritize clear, descriptive, and meaningful names for variables, functions, and types.
- Avoid arbitrary or temporary names that increase cognitive load.
- Good names clarify intent and reduce confusion, especially in large codebases.

### Say No When Needed

- Decline changes that don't meet quality standards, even if it's uncomfortable.
- Be objective and explain your reasoning clearly.
- Suggest alternatives and focus on improvement, not personal criticism.
- Avoid setting precedents that lead to technical debt.

### Iterate

- Treat code reviews as an iterative process, not a one-time event.
- Start with the big picture, then move to details in subsequent rounds.
- Aim for high-quality code, not just quick merges.

### Run The Code

- Run the code, tests, and linters locally if you can.
- Experiment with the changes to better understand their impact.
- User-facing changes are easier to evaluate by actually using the software.

### Avoid Nitpicking

- Leave formatting and whitespace to automated tools.
- Focus on logic, design, maintainability, and correctness.
- Only raise issues that impact code quality or future maintainability.

### Explain Why

- Explain the reasoning behind your feedback.
- Provide alternatives and supporting documentation when possible.
- Aim for feedback that helps the author grow and avoid future mistakes.

### Ask Questions

- Ask for clarification if you don't understand something.
- Your questions may reveal missing documentation or unclear logic.
- Encourage open discussion and learning for everyone involved.

## Communication

### Giving Feedback

- Remember that reviews are about people as much as code.
- Build trust and understanding, ideally through pair reviews or open discussion.
- Give feedback that you would appreciate receiving yourself.

### Be Kind

- Be respectful and constructive, even when disagreeing.
- Use Socratic questions to encourage thoughtful discussion.
- Add positive comments to motivate and acknowledge good work.

### Be Upfront

- Communicate proactively if you can't review code promptly.
- Set clear expectations to avoid frustration and bottlenecks.

## Continuous Improvement

### Keep Learning

- Use code reviews as an opportunity to learn new techniques and perspectives.
- Aim to learn something new with each review.

### Get Feedback

- Occasionally ask authors for feedback on your reviews.
- Reflect on whether your feedback was helpful, timely, and focused on the right issues.
- Continuously refine your review process and communication style.
