# Maintainer Notes

## Scope

This repository provides reusable workflow structure. It does not call model APIs, store credentials, or choose a model for the user.

## Release checklist

1. Review open issues and confirm the intended scope.
2. Run `pytest` on every supported Python version.
3. Update `CHANGELOG.md` and the version in the package.
4. Build the package and inspect its contents.
5. Tag the verified commit and write concise release notes.

## Triage

Bug reports should include a minimal command or code sample, expected behavior, actual behavior, and Python version. Feature requests should explain the maintenance problem before proposing a format or API.

## Compatibility

The public Python API consists of the names exported from `ai_workflow_toolkit.__init__`. CLI commands and documented template names should remain backward compatible within a minor release.
