import json
import os
import sys

from github import Github

event_jsonfile = os.environ['GITHUB_EVENT_PATH']

with open(event_jsonfile, encoding='utf-8') as fin:
    event = json.load(fin)

pr_num = event['number']
reponame = event['pull_request']['base']['repo']['full_name']
g = Github(os.environ.get('GITHUB_TOKEN'))
repo = g.get_repo(reponame)
try:
    pr = repo.get_pull(pr_num)
except Exception:
    # GitHub Actions all milestoned/demilestoned events as issue event,
    # so if this is issue and not PR, it is no-op.
    pass
else:
    if pr.milestone:
        print('This pull request has a milestone set.')
    else:
        print('Maintainers need to set the milestone for this pull request.')
        sys.exit(1)
