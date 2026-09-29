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