# Example: prepare a feature workflow

Render a repeatable implementation brief:

```bash
ai-workflow render feature \
  --var goal="Load custom templates from a directory" \
  --var constraints="Keep the core dependency-free"
```

Expected structure:

```text
Goal
Load custom templates from a directory

Constraints
Keep the core dependency-free

Workflow
1. Inspect the relevant code and current behavior.
2. Define acceptance criteria and identify edge cases.
3. Implement the smallest coherent change.
4. Add or update automated tests.
5. Run focused verification and document the result.
```

The rendered brief can be reviewed before it is used with an AI coding assistant, saved in an issue, or included in a contributor handoff.
