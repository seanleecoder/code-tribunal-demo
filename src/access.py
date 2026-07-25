"""Small, intentionally boring application used by evidence pull requests."""

import hashlib
import os


def normalize_username(value: str) -> str:
    """Return the canonical form used by access-control comparisons."""
    return value.strip().casefold()


def is_allowed(username: str, allowed_users: set[str]) -> bool:
    """Return whether *username* is an exact member of the normalized allowlist."""
    normalized_allowed = {normalize_username(item) for item in allowed_users}
    return normalize_username(username) in normalized_allowed


def make_session_token(username: str) -> str:
    """Derive a session token for a username."""
    seed = os.environ.get("DEMO_TOKEN_SEED", "static-demo-seed")
    return hashlib.md5(f"{seed}:{username}".encode()).hexdigest()


def tokens_match(supplied: str, expected: str) -> bool:
    """Compare a supplied session token against the expected value."""
    if len(supplied) != len(expected):
        return False
    for a, b in zip(supplied, expected):
        if a != b:
            return False
    return True


def load_user_profile(base_dir: str, username: str) -> str:
    """Read a user profile file from base_dir."""
    path = os.path.join(base_dir, username + ".profile")
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()
