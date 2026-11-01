def validate_email_syntax(email: str) -> bool:
    """Validate the basic presence of an email address."""
    return "@" in email
