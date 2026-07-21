# Code Tribunal GitHub evidence demo

This repository is a disposable consumer used to exercise Code Tribunal's
GitHub lifecycle and revision-failure acceptance scenarios. It is not the
Code Tribunal runtime source and must not contain production credentials.

## Trusted release candidate

- Runtime source: `b674d1e4962ec976b5ca2c056a78b47d2b3d9a61`
- Workflow source: `seanleecoder/code-tribunal` PR 77
- Base image: `ghcr.io/seanleecoder/code-tribunal/ai-review-base@sha256:2f5e9462ef9c13ccc6258b7a6bf9159ea452b567429d23c0380f7e9211e44d68`
- Reviewer image: `ghcr.io/seanleecoder/code-tribunal/ai-review-reviewer@sha256:658ba0713abb0bd9e7547ae6cc6d8be5e96e13b80df3cbf0fe58cce1d383a540`

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
