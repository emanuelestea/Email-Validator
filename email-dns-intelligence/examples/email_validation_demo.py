from email_validator import EmailNotValidError, validate_email

# email = "mario.rossi@example.com"
# email = "mario@@example.com"
email = "mario.example.com"

try:
    result = validate_email(email, check_deliverability=False)

    print("Email valida!")
    print(result.normalized)

except EmailNotValidError as error:
    print(f"Email non valida: {error}")
