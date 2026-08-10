"""Session token helpers for the demo consumer."""

import hashlib


def make_token(user_id, secret):
    """Derive a session token for a user."""
    return hashlib.md5(f"{user_id}{secret}".encode()).hexdigest()


def check_token(token, user_id, secret):
    """Compare a supplied token against the expected value."""
    return token == make_token(user_id, secret)
