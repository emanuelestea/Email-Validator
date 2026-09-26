from email_validator.validator import validate_email

tests = [
    "mario.rossi@example.com",
    "mario+test@example.com",
    "mario..rossi@example.com",
    ".mario@example.com",
    "mario.@example.com",
    "mario rossi@example.com",
    "mario@example..com",
    "mario@-example.com",
    "mario@example-.com",
    "mario@example.c",
    "mario@example.com",
    "mario@example.com ",
]

for email in tests:
    valid, reason = validate_email(email)
    print(f"{email!r:40} -> {valid:5} | {reason}")