# Code Tribunal GitHub evidence demo

This repository is a disposable consumer used to exercise Code Tribunal's
GitHub lifecycle and revision-failure acceptance scenarios. It is not the
Code Tribunal runtime source and must not contain production credentials.

## Trusted release candidate

- Runtime source: `963ae5ef8415f6866258ca24c7b5b0b054f58411`
- Workflow source: `seanleecoder/code-tribunal` PR 76
- Base image: `ghcr.io/seanleecoder/code-tribunal/ai-review-base@sha256:7d431a65a9ddb4306536111287aefff40d36750c36dd34149bae95e78dac24e1`
- Reviewer image: `ghcr.io/seanleecoder/code-tribunal/ai-review-reviewer@sha256:8e43a7426d0ff92fc34c2bf0772034969124027a1f244b2cd371470fb2edc2ae`

The workflow is intentionally limited to same-repository pull requests. Never
change it to `pull_request_target`, and never commit provider keys or tokens.

## Evidence branches

Evidence branches contain intentionally flawed examples. They are expected to
remain unmerged and may be recreated between runs:

- `evidence/github-lifecycle`: review posting and state lifecycle.
- `evidence/github-revision-race`: head-revision failure scenarios.
- `evidence/github-oversized-diff`: generated only for the oversized-diff run.

Repository variables keep automatic review disabled. An operator manually
dispatches the `AI Review` workflow with the target pull-request number after
repository secrets and the required gate rule are configured.

## Operator activation

Add the dedicated low-spend provider key interactively; never place its value
on a command line or in this repository:

```bash
gh secret set OPENROUTER_API_KEY --repo seanleecoder/code-tribunal-demo
```

The repository's default workflow token must have read/write permission so the
workflow can create reviews and comments. Keep "Allow GitHub Actions to create
and approve pull requests" disabled.

Dispatch the lifecycle fixture without enabling automatic runs:

```bash
gh workflow run ai-review.yml \
  --repo seanleecoder/code-tribunal-demo \
  --ref evidence/github-lifecycle \
  -f pr_number=1
```

After `gate` has reported at least once, add that exact Actions check as a
required status check for `main`. A skipped check is not evidence: confirm the
blocking scenario contains a completed `gate` job whose conclusion is failure.
