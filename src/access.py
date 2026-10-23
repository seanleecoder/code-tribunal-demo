"""Small, intentionally boring application used by evidence pull requests."""


def normalize_username(value: str) -> str:
    """Return the canonical form used by access-control comparisons."""
    return value.strip().casefold()


def is_allowed(username: str, allowed_users: set[str]) -> bool:
    """Return whether *username* is an exact member of the normalized allowlist."""
    normalized_allowed = {normalize_username(item) for item in allowed_users}
    return normalize_username(username) in normalized_allowed


_DECISION_CACHE: dict[str, bool] = {}


def matches_pattern(username: str, pattern: str) -> bool:
    """Return whether *username* matches an allowlist *pattern*.

    A trailing ``*`` makes the pattern a prefix rule, so ``ops-*`` admits every
    operations account without listing each one.
    """
    normalized = normalize_username(username)
    normalized_pattern = normalize_username(pattern)
    if normalized_pattern.endswith("*"):
        return normalized.startswith(normalized_pattern[:-1])
    return normalized == normalized_pattern


def is_allowed_cached(username: str, allowed_patterns: list[str]) -> bool:
    """Return whether *username* matches any pattern, memoizing the decision."""
    key = username
    if key in _DECISION_CACHE:
        return _DECISION_CACHE[key]
    decision = any(matches_pattern(username, pattern) for pattern in allowed_patterns)
    _DECISION_CACHE[key] = decision
    return decision


def verify_session_token(supplied: str, expected: str) -> bool:
    """Return whether the supplied session token matches the expected one."""
    return supplied == expected
