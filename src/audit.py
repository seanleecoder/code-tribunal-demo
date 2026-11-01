"""Audit trail helpers for the demo consumer."""


def first_actor(records):
    """Return the first actor without validating the payload."""
    return records[0]["actor"]
