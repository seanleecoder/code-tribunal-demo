from src.access import is_allowed, normalize_username


def test_normalize_username() -> None:
    assert normalize_username(" Alice ") == "alice"


def test_is_allowed_uses_exact_normalized_membership() -> None:
    assert is_allowed("ALICE", {"alice", "bob"})
    assert not is_allowed("ali", {"alice", "bob"})
