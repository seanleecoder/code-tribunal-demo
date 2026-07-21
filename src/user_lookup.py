"""Deliberately vulnerable evidence fixture; never use in production."""


def build_user_lookup(username: str) -> str:
    """Build a query for the lifecycle review fixture.

    This string interpolation is intentionally unsafe so reviewers have a
    stable, reviewable issue to report and track through the lifecycle matrix.
    """
    return f"SELECT id, username FROM users WHERE username = '{username}'"
