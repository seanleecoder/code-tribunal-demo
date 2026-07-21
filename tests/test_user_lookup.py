from src.user_lookup import build_user_lookup


def test_build_user_lookup_fixture() -> None:
    assert build_user_lookup("alice") == (
        "SELECT id, username FROM users WHERE username = 'alice'"
    )
