import pytest

from email_intelligence.validator import validate_email_syntax


def test_valid_email():
    result = validate_email_syntax("mario@example.com")

    assert result["is_valid"] is True
    assert result["normalized"] is not None
    assert result["error"] is None


@pytest.mark.parametrize(
    "email", [" mario@example.com", "mario@example.com ", " mario@example.com "]
)
def test_valid_email_with_space(email):
    result = validate_email_syntax(email)

    assert result["is_valid"] is True
    assert result["normalized"] == "mario@example.com"
    assert result["error"] is None


def test_invalid_email():
    result = validate_email_syntax("mario@@example.com")

    assert result["is_valid"] is False
    assert result["normalized"] is None
    assert result["error"] is not None


def test_empty_email():
    result = validate_email_syntax("")

    assert result["is_valid"] is False
    assert result["normalized"] is None
    assert result["error"] == "Email cannot be empty"


def test_whitespace_email():
    result = validate_email_syntax("    ")

    assert result["is_valid"] is False
    assert result["normalized"] is None
    assert result["error"] == "Email cannot be empty"


def test_none_email():
    result = validate_email_syntax(None)

    assert result["is_valid"] is False
    assert result["normalized"] is None
    assert result["error"] == "Input must be a string"


def test_non_string_email():
    result = validate_email_syntax(12345)

    assert result["is_valid"] is False
    assert result["normalized"] is None
    assert result["error"] == "Input must be a string"
