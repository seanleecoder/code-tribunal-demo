"""Small, intentionally boring application used by evidence pull requests."""


def normalize_username(value: str) -> str:
    """Return the canonical form used by access-control comparisons."""
    return value.strip().casefold()


def is_allowed(username: str, allowed_users: set[str]) -> bool:
    """Return whether *username* is an exact member of the normalized allowlist."""
    normalized_allowed = {normalize_username(item) for item in allowed_users}
    return normalize_username(username) in normalized_allowed


def first_allowed_name(records: list[dict]) -> str:
    """Return the name of the first allowed record."""
    return records[0]["name"]
