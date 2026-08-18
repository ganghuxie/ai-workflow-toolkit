import json

import pytest

from ai_workflow_toolkit.cli import main
from ai_workflow_toolkit.templates import (
    available_workflows,
    get_workflow,
    render_workflow,
)


def test_available_workflows_are_sorted():
    names = [workflow.name for workflow in available_workflows()]
    assert names == sorted(names)
    assert {"feature", "bugfix", "review", "docs", "release"} <= set(names)


def test_render_feature_workflow():
    result = render_workflow(
        "feature",
        goal="Add YAML support",
        constraints="Keep backward compatibility",
    )
    assert "Add YAML support" in result
    assert "Keep backward compatibility" in result
    assert "automated tests" in result


def test_missing_variable_has_helpful_error():
    with pytest.raises(ValueError, match="constraints"):
        render_workflow("feature", goal="Add YAML support")


def test_unknown_workflow_lists_choices():
    with pytest.raises(KeyError, match="Available:"):
        get_workflow("missing")


def test_cli_lists_workflows(capsys):
    assert main(["list"]) == 0
    assert "feature:" in capsys.readouterr().out


def test_cli_json_output(capsys):
    assert (
        main(
            [
                "render",
                "docs",
                "--var",
                "goal=Explain installation",
                "--var",
                "audience=Python developers",
                "--json",
            ]
        )
        == 0
    )
    payload = json.loads(capsys.readouterr().out)
    assert payload["name"] == "docs"
    assert "Explain installation" in payload["content"]
