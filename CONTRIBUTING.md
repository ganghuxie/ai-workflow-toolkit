# Contributing

Thank you for helping improve AI Workflow Toolkit.

## Before opening a change

1. Search existing issues and open a focused issue when the behavior needs discussion.
2. Keep each pull request limited to one problem.
3. Add or update tests for behavior changes.
4. Update documentation when users will notice the change.

## Local setup

```bash
git clone https://github.com/ganghuxie/ai-workflow-toolkit.git
cd ai-workflow-toolkit
python -m venv .venv
python -m pip install -e ".[dev]"
pytest
```

## Template guidelines

A workflow should have one clear purpose, explicit inputs, actionable steps, and a verification phase. Avoid templates that depend on a specific commercial model or expose secrets.

## Commit messages

Use short imperative messages such as `Add YAML template loader` or `Clarify missing-variable error`.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
