import json
import os
import sys

from github import Github

event_name = os.environ['GITHUB_EVENT_NAME']
if event_name not in ('pull_request_target', 'pull_request'):
    print(f'No-op for {event_name}')
    sys.exit(0)

event_jsonfile = os.environ['GITHUB_EVENT_PATH']

with open(event_jsonfile, encoding='utf-8') as fin:
    event = json.load(fin)

pr_num = event['number']
reponame = event['pull_request']['base']['repo']['full_name']
g = Github(os.environ.get('GITHUB_TOKEN'))
repo = g.get_repo(reponame)
pr = repo.get_pull(pr_num)
if pr.milestone:
    print('This pull request has a milestone set.')
else:
    print('Maintainers need to set the milestone for this pull request.')
    sys.exit(1)
