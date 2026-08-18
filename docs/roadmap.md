# Roadmap

AI Workflow Toolkit is intentionally small. The roadmap prioritizes features that keep workflows portable, reviewable, and easy to automate.

## Near term

- Load user-defined templates from a project or user directory
- Define a documented YAML format for templates
- Validate template metadata and required variables
- Add integration examples for common open-source maintenance tasks
- Improve CLI error messages and exit-code coverage

## Later

- Compose several workflows into a checked sequence
- Export rendered workflows as Markdown or JSON files
- Offer an optional template catalog without adding core runtime dependencies
- Add localization hooks for workflow descriptions

## Principles

- Keep the core package dependency-free
- Prefer explicit files over hidden state
- Make output inspectable before it is sent to an AI tool
- Add features with tests and user-facing documentation

Discussion and focused proposals are welcome in GitHub Issues.
