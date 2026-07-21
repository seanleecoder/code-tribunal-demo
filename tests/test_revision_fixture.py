from src.revision_fixture import REVISION_MARKER


def test_revision_marker() -> None:
    assert REVISION_MARKER == "initial"
