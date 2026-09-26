from email_validator.validator import validate_email


valid_emails = [
    "mario.rossi@example.com",
    "mario+test@example.com",
    "mario@example.com",
]


invalid_emails = [
    "mario..rossi@example.com",
    ".mario@example.com",
    "mario.@example.com",
    "mario rossi@example.com",
    "mario@example..com",
    "mario@-example.com",
    "mario@example-.com",
    "mario@example.c",
    "mario@example.com ",
]


def test_email_valida():
    for email in valid_emails:
        assert validate_email(email)[0] == True


def test_email_non_valida():
    for email in invalid_emails:
        risultato, messaggio = validate_email(email)

        print(f"{email} -> {risultato}: {messaggio}")

        assert risultato == False