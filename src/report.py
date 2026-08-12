"""Added-file fixture for the deterministic mock lifecycle chain."""


def first_record(records: list[dict]) -> dict:
    """Return the first record in the batch."""
    return records[0]
