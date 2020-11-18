# action-check_milestone_exists

**Blocked by:** https://github.community/t/feature-request-add-milestone-changes-as-activity-type-to-pull-request/16778/7

Check if milestone is assigned. Create a `.github/workflows/check_pr_milestone.yml` with this:

```
name: Check PR milestone

on:
  pull_request_target:
    types: [opened, milestoned, demilestoned]

jobs:
  milestone:
    name: Check if milestone is set
    runs-on: ubuntu-latest
    steps:
    - name: Check milestone
      uses: pllim/action-check_milestone_exists@main
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
