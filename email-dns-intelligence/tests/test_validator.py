from email_intelligence.validator import validate_email_syntax


def test_validate_email_syntax_with_at_symbol():
    assert validate_email_syntax("test@example.com") is True


def test_validate_email_syntax_without_at_symbol():
    assert validate_email_syntax("invalid-email") is False
