# Intentional Demo Bugs

This file is for the person recording the demonstration. The defects below are deliberately seeded and are not production code.

1. **Discount calculation:** `apply_discount` subtracts the percentage number directly instead of calculating that percentage of the price.
2. **Average calculation:** `calculate_average` divides by `len(values) + 1`, producing an incorrect mean for non-empty lists.
3. **Username normalization:** `normalize_username` lowercases text but does not trim leading or trailing whitespace.

## Suggested XAI Code Agent demo sequence

1. Ask for a read-only analysis of the repository. Confirm no files, commits, or branches are changed.
2. Ask it to identify likely bugs and explain their impact.
3. Ask it to propose fixes for the three functions.
4. Review the proposed diff before approving anything.
5. Approve the fix and verify that the agent uses a separate branch and opens a pull request, if those features work in the current deployment.
6. Check the GitHub Actions test run on the pull request.

Do not tell the agent to modify files during the read-only analysis step. Do not merge the pull request until the demo is complete.
