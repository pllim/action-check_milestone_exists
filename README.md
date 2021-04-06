# Archived: Use github-script

When GitHub Actions support proper PR milestone events, use this instead:

```yaml
name: Check PR milestone

on:
  pull_request:
    types: [opened, milestoned, demilestoned]

jobs:
  milestone:
    name: Check if milestone is set
    runs-on: ubuntu-latest
    steps:
    - name: Check milestone
      uses: actions/github-script@v3
      with:
        script: |
          const pr = context.payload.pull_request;
          if (pr.milestone) {
            core.info(`This pull request has a milestone set: ${pr.milestone.title}`);
          } else {
            core.setFailed("A maintainer needs to set the milestone for this pull request.");
          }
```

# GitHub Action to check if PR milestone is set

**Blocked by:** https://github.community/t/feature-request-add-milestone-changes-as-activity-type-to-pull-request/16778/7
(Until this is fixed, this Action would not run when PR has milestone set
or removed.)

Check if milestone is assigned. Create a `.github/workflows/check_pr_milestone.yml` with this:

```yaml
name: Check PR milestone

on:
  pull_request:
    types: [opened, milestoned, demilestoned]

jobs:
  milestone:
    name: Check if milestone is set
    runs-on: ubuntu-latest
    steps:
    - name: Check milestone
      uses: pllim/action-check_milestone_exists@main
```
