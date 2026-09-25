# 📧 Email Validator

A lightweight and extensible tool for validating email addresses.
The project checks an email address through multiple validation steps, providing a clear result for each check.

🚧 This project is currently under development.


## Features

 - Email syntax validation
 - Domain validation
 - DNS / MX record verification
 - Disposable email detection
 - SMTP verification
 - Bulk email validation
 - CSV import/export
 - Validation reports

## Installation

Clone the repository:
 - git clone https://github.com/emanuelestea/email-validator.git

## Usage

Example Input:

> from email_validator import validate

> result = validate("example@example.com")

Example output:

> Email: example@example.com
Syntax:      ✓
Domain:      ✓
MX Record:   ✓
Disposable:  ✗
Status: VALID


## Roadmap
**v0.1.0**:
 - Basic syntax validation
 - Initial project structure
 - Unit tests

**v0.2.0**
 - Domain validation
 - DNS / MX checks

**v0.3.0**
 - Disposable email detection

**v0.4.0**
 - SMTP verification

**v0.5.0**
 - CSV bulk validation



## ⚠️ Limitations

Email validation cannot guarantee that a mailbox actually exists.

Some mail servers intentionally prevent external verification, while others accept messages for any address on their domain.

For this reason, the validator reports whether an address is likely valid rather than guaranteeing that the mailbox exists.

## AI-Assisted Development
This project is also being developed with the support of AI tools, primarily ChatGPT, as a learning and experimentation aid.

AI is currently used for:
 - Brainstorming — exploring ideas, possible features, architecture choices and implementation approaches.
 - Planning — breaking the project into smaller tasks and defining development milestones.
 - Progress tracking — maintaining a development log to monitor the current state of the project, completed tasks and next steps.

## 🤝 Contributing

Contributions, suggestions and bug reports are welcome.
Feel free to open an issue or submit a pull request.


Made with ❤️ for learning, experimentation and practical use.
