# AI Workflow Toolkit

A lightweight open-source toolkit for building repeatable AI-assisted development workflows.

The project turns reusable prompt templates into structured, reviewable workflow briefs. It is designed for independent developers and open-source maintainers who want consistent context gathering, implementation, review, documentation, and release routines.

## Features

- Built-in workflows for feature development, bug fixing, code review, documentation, and release preparation
- Small Python API with no runtime dependencies
- Command-line interface with text and JSON output
- Template variables and clear validation errors
- Tests, contribution guidelines, issue templates, and a public roadmap

## Quick start

Requires Python 3.9 or later.

```bash
python -m pip install -e .
ai-workflow list
ai-workflow render feature --var goal="Add YAML template support" --var constraints="Keep backward compatibility"
```

JSON output is useful for scripts and agent integrations:

```bash
ai-workflow render bugfix --var problem="CLI exits without a useful message" --json
```

## Python API

```python
from ai_workflow_toolkit import render_workflow

brief = render_workflow(
    "feature",
    goal="Add project-local templates",
    constraints="No runtime dependencies",
)
print(brief)
```

## Built-in workflows

| Name | Purpose |
| --- | --- |
| `feature` | Plan and implement a scoped feature |
| `bugfix` | Reproduce, diagnose, fix, and verify a defect |
| `review` | Review code for correctness and maintainability |
| `docs` | Improve documentation around a concrete reader goal |
| `release` | Prepare a small, verifiable software release |

## Development

```bash
python -m pip install -e ".[dev]"
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md), the [roadmap](docs/roadmap.md), and [maintainer notes](docs/maintainer-notes.md).

## Project status

This is an early-stage project maintained in public. Feedback, focused issues, documentation fixes, and workflow-template contributions are welcome.

## License

MIT
