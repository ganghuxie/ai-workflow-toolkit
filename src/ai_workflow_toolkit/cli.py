"""Command-line interface for AI Workflow Toolkit."""

import argparse
import json
from typing import Dict, Optional, Sequence

from .templates import available_workflows, get_workflow


def _variable(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("variables must use NAME=VALUE")
    name, content = value.split("=", 1)
    if not name or not content:
        raise argparse.ArgumentTypeError("variable name and value cannot be empty")
    return name, content


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-workflow",
        description="Render reusable AI-assisted development workflows.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list", help="List built-in workflows")

    render = subparsers.add_parser("render", help="Render a workflow")
    render.add_argument("name", help="Workflow name")
    render.add_argument(
        "--var",
        action="append",
        default=[],
        type=_variable,
        metavar="NAME=VALUE",
        help="Template variable; repeat for multiple values",
    )
    render.add_argument("--json", action="store_true", help="Output JSON")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "list":
        for workflow in available_workflows():
            variables = ", ".join(workflow.variables)
            print(f"{workflow.name}: {workflow.description} [{variables}]")
        return 0

    try:
        workflow = get_workflow(args.name)
        values: Dict[str, str] = dict(args.var)
        rendered = workflow.render(values)
    except (KeyError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc

    if args.json:
        print(
            json.dumps(
                {"name": workflow.name, "variables": values, "content": rendered},
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
