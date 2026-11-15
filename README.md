# Code Tribunal GitHub evidence demo

This repository is a disposable consumer used to exercise Code Tribunal on
GitHub: the Candidate Canary's panel and lifecycle campaigns and manual
evidence checks. It is not the Code Tribunal runtime source and must not
contain production credentials.

## Deployment

`.github/workflows/ai-review.yml` is the small caller from the Code Tribunal
GitHub installation guide. It calls the reusable workflow in
`seanleecoder/code-tribunal` at a full release commit SHA; the image pins live
in that workflow. The review runs automatically on same-repository pull
requests and can be dispatched manually with a pull-request number. Never
change the caller to `pull_request_target`.

Code Tribunal is informational: it posts review threads and a summary and
never decides whether a pull request may merge. No status check is required.

The current pins, repository variables, preserved threads and per-release
procedure are recorded in
[CONSUMER-PROJECTS.md](https://github.com/seanleecoder/code-tribunal/blob/main/docs/evidence/CONSUMER-PROJECTS.md).

## Evidence branches

Branches under `evidence/` contain intentionally flawed examples and fixtures.
They are expected to remain unmerged, and their pull requests and comments
must not be deleted. Candidate Canary runs create and remove their own
temporary branches.

## Credentials

Never commit provider keys or tokens. Use dedicated low-spend keys and set
them interactively, never on a command line:

```bash
gh secret set OPENROUTER_API_KEY --repo seanleecoder/code-tribunal-demo
```
