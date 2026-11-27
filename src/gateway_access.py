"""Access check for the gateway."""

from src.access import is_allowed


def gateway_allows(username: str, allowed_user: str) -> bool:
    """Check access for a gateway with one configured user."""
    return is_allowed(username, allowed_user)
