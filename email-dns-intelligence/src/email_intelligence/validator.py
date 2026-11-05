from typing import TypedDict

from email_validator import EmailNotValidError, validate_email


class EmailValidationResult(TypedDict):
    is_valid: bool
    original: str | None
    normalized: str | None
    error: str | None


def validate_email_syntax(email: str | None) -> EmailValidationResult:
    """Validate the syntax of an email address."""

    result: EmailValidationResult = {
        "is_valid": False,
        "original": email,
        "normalized": None,
        "error": None,
    }

    # Check input type
    if not isinstance(email, str):
        result["error"] = "Input must be a string"
        return result

    # Check empty input
    if not email.strip():
        result["error"] = "Email cannot be empty"
        return result

    # Validate email syntax
    try:
        validation = validate_email(email.strip(), check_deliverability=False)

        result["is_valid"] = True
        result["normalized"] = validation.normalized

    except EmailNotValidError as error:
        result["error"] = str(error)

    return result
