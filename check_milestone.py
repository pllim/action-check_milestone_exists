import json
import os

from baldrick.github.github_api import PullRequestHandler

MISSING_MESSAGE = 'Maintainers need to set the milestone for this pull request.'  # noqa
PRESENT_MESSAGE = 'This pull request has a milestone set.'

event_jsonfile = os.environ['GITHUB_EVENT_PATH']
reponame = os.environ['GITHUB_REPOSITORY']

with open(event_jsonfile) as fin:
    event = json.load(fin)

pr_num = event['number']
pr_handler = PullRequestHandler(reponame, pr_num)

if pr_handler.milestone:
    result = {'name': "milestone: present",
              'title': PRESENT_MESSAGE,
              'conclusion': 'success',
              'summary': ''}
else:
    result = {'name': "milestone: absent",
              'title': MISSING_MESSAGE,
              'conclusion': 'failure',
              'summary': ''}

key = 'milestone'
set_check = False

# only_ours only work for Flask app
existing_checks = pr_handler.list_checks(only_ours=False)

# Only update if things have changed or not yet exist
if key in existing_checks:
    old_conclusion = existing_checks[key]['conclusion']
    if old_conclusion != result['conclusion']:
        set_check = True
else:
    set_check = True

if set_check:
    pr_handler.set_check(key, result['title'], name=result['name'],
                         summary=result['summary'],
                         conclusion=result['conclusion'])
