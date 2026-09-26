from email_validator.validator import validate_email


valid_emails = [
    "mario.rossi@example.com",
    "mario+test@example.com",
    "mario@example.com",
]

invalid_locals = [
    "mario..rossi@example.com",
    ".mario@example.com",
    "mario.@example.com",
    "mario rossi@example.com"
]

invalid_domains = [
    "mario..rossi@example.com",
    ".mario@example.com",
    "mario.@example.com",
    "mario rossi@example.com"
]


def test_email_valida():
    for email in valid_emails:
        assert validate_email(email)[0] == True


def test_email_non_valida():
    for email in invalid_locals:
        risultato, messaggio = validate_email(email)

        print(f"{email} -> {risultato}: {messaggio}")

        assert risultato == False

    for email in invalid_domains:
        risultato, messaggio = validate_email(email)

        print(f"{email} -> {risultato}: {messaggio}")

        assert risultato == False