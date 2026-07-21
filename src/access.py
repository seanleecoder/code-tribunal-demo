"""Small, intentionally boring application used by evidence pull requests."""


def normalize_username(value: str) -> str:
    """Return the canonical form used by access-control comparisons."""
    return value.strip().casefold()


def is_allowed(username: str, allowed_users: set[str]) -> bool:
    """Return whether *username* is an exact member of the normalized allowlist."""
    normalized_allowed = {normalize_username(item) for item in allowed_users}
    return normalize_username(username) in normalized_allowed


# Unrelated line-movement marker for lifecycle identity evidence.
def build_user_lookup(username: str) -> str:
    """Deliberately vulnerable lifecycle fixture; never use in production.

    The interpolation is intentionally unsafe so reviewers have a stable issue
    anchored to an existing tracked file for create/update/resolve testing.
    """
    return (
        f"SELECT id, username, email FROM users WHERE username = '{username}'"
    )
