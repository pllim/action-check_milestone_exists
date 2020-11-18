import json
import os
import sys

from github import Github

event_jsonfile = os.environ['GITHUB_EVENT_PATH']

with open(event_jsonfile) as fin:
    event = json.load(fin)

pr_num = event['number']
reponame = os.environ['GITHUB_REPOSITORY']
g = Github(os.environ.get('GITHUB_TOKEN'))
repo = g.get_repo(reponame)
pr = repo.get_pull(pr_num)

if not pr.milestone:
    print('Maintainers need to set the milestone for this pull request.')
    sys.exit(1)

print('This pull request has a milestone set.')
