import * as core from "@actions/core";
import * as github from "@actions/github";

async function run() {
    try {
        const pr = github.context.payload.pull_request;
        if (!pr) {
            core.info("This action only runs for pull request, exiting with no-op");
            return;
        }

        if (pr.milestone) {
            core.info(`This pull request has a milestone set: ${pr.milestone.title}`);
        } else {
            core.setFailed("A maintainer needs to set the milestone for this pull request.");
        }
    } catch(err) {
        core.setFailed(`Action failed with error ${err}`);
    }
}

run();
