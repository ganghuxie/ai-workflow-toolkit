"""Built-in workflow templates and rendering helpers."""

from dataclasses import dataclass
from string import Formatter
from typing import Dict, Iterable, Mapping, Tuple


@dataclass(frozen=True)
class WorkflowTemplate:
    """A named workflow that can be rendered with user-provided variables."""

    name: str
    description: str
    template: str

    @property
    def variables(self) -> Tuple[str, ...]:
        names = {
            field_name
            for _, field_name, _, _ in Formatter().parse(self.template)
            if field_name
        }
        return tuple(sorted(names))

    def render(self, values: Mapping[str, str]) -> str:
        missing = [name for name in self.variables if not values.get(name)]
        if missing:
            joined = ", ".join(missing)
            raise ValueError(f"Missing required variables: {joined}")
        return self.template.format_map(dict(values)).strip()


_WORKFLOWS: Dict[str, WorkflowTemplate] = {
    "feature": WorkflowTemplate(
        name="feature",
        description="Plan and implement a scoped feature.",
        template="""Goal
{goal}

Constraints
{constraints}

Workflow
1. Inspect the relevant code and current behavior.
2. Define acceptance criteria and identify edge cases.
3. Implement the smallest coherent change.
4. Add or update automated tests.
5. Run focused verification and document the result.
""",
    ),
    "bugfix": WorkflowTemplate(
        name="bugfix",
        description="Reproduce, diagnose, fix, and verify a defect.",
        template="""Problem
{problem}

Expected behavior
{expected}

Workflow
1. Reproduce the failure with the smallest reliable case.
2. Trace the failing path and identify the root cause.
3. Add a regression test.
4. Apply a focused fix without unrelated refactoring.
5. Run the regression test and relevant surrounding tests.
""",
    ),
    "review": WorkflowTemplate(
        name="review",
        description="Review code for correctness and maintainability.",
        template="""Review target
{target}

Context
{context}

Workflow
1. Identify correctness and security risks.
2. Check behavioral regressions and compatibility.
3. Evaluate error handling and edge cases.
4. Check whether tests cover the changed behavior.
5. Report actionable findings ordered by severity.
""",
    ),
    "docs": WorkflowTemplate(
        name="docs",
        description="Improve documentation around a reader goal.",
        template="""Reader goal
{goal}

Audience
{audience}

Workflow
1. Verify the documented behavior against the implementation.
2. Put the outcome and shortest working example first.
3. Explain prerequisites and failure cases.
4. Use consistent terminology and runnable examples.
5. Review links, commands, and formatting.
""",
    ),
    "release": WorkflowTemplate(
        name="release",
        description="Prepare a small, verifiable software release.",
        template="""Release
{version}

Summary
{summary}

Workflow
1. Confirm the intended changes and version number.
2. Run the complete test suite.
3. Update the changelog and user-facing documentation.
4. Build and inspect release artifacts.
5. Tag only the verified commit and publish release notes.
""",
    ),
}


def available_workflows() -> Iterable[WorkflowTemplate]:
    """Return built-in workflows in name order."""
    return tuple(_WORKFLOWS[name] for name in sorted(_WORKFLOWS))


def get_workflow(name: str) -> WorkflowTemplate:
    """Return a workflow by name, with a helpful error for unknown names."""
    try:
        return _WORKFLOWS[name]
    except KeyError as exc:
        choices = ", ".join(sorted(_WORKFLOWS))
        raise KeyError(f"Unknown workflow '{name}'. Available: {choices}") from exc


def render_workflow(name: str, **values: str) -> str:
    """Render a built-in workflow."""
    return get_workflow(name).render(values)
