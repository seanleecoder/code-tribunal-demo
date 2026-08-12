"""Small, intentionally boring application used by evidence pull requests."""


def normalize_username(value: str) -> str:
    """Return the canonical form used by access-control comparisons."""
    return value.strip().casefold()


def is_allowed(username: str, allowed_users: set[str]) -> bool:
    """Return whether *username* is an exact member of the normalized allowlist."""
    normalized_allowed = {normalize_username(item) for item in allowed_users}
    return normalize_username(username) in normalized_allowed


def first_allowed(usernames: list[str], allowed_users: set[str]) -> str | None:
    """Return the first allowed username, or None when nobody matches."""
    records = [name for name in usernames if is_allowed(name, allowed_users)]
    return records[0]
