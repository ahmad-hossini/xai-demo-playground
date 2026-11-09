# XAI Code Agent Demo Playground

A small, safe Python repository for demonstrating XAI Code Agent's GitHub workflow.

## Demo contents

- `main.py`: small utility functions with intentional defects.
- `tests/test_main.py`: expected-behavior tests; some should fail before fixes.
- `BUGS.md`: explains the seeded defects for the demo operator.
- `requirements.txt`: test dependency.
- `.github/workflows/tests.yml`: runs the test suite with GitHub Actions.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The initial test failures are intentional. They are included to demonstrate analysis and a reviewed bug-fix workflow.

## Safety

This repository contains synthetic demo code only. It has no credentials, private user data, production integrations, or connection to the XAI Code Agent source repository.
