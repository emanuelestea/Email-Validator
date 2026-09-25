Email Validator

A lightweight and extensible tool for validating email addresses.

The project checks an email address through multiple validation steps, providing a clear result for each check.

🚧 This project is currently under development.

✨ Features

 Email syntax validation

 Domain validation

 DNS / MX record verification

 Disposable email detection

 SMTP verification

 Bulk email validation

 CSV import/export

 Validation reports

🔍 How it works

The validator performs multiple checks on an email address:

Email address
      │
      ▼
┌───────────────┐
│ Syntax check  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Domain check  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   DNS / MX    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  Disposable?  │
└───────┬───────┘
        │
        ▼
      Result


The goal is to provide a more useful result than a simple regular-expression check.

📦 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/email-validator.git
cd email-validator


Create a virtual environment:

python -m venv .venv


Activate it:

Windows
.venv\Scripts\activate

Linux / macOS
source .venv/bin/activate


Install the project:

pip install -e .

🚀 Usage

Example:

from email_validator import validate

result = validate("example@example.com")

print(result)


Example output:

Email: example@example.com
Syntax:      ✓
Domain:      ✓
MX Record:   ✓
Disposable:  ✗

Status: VALID

🧪 Tests

Run the test suite with:

pytest

🏗️ Project Structure
email-validator/
├── src/
│   └── email_validator/
│       ├── core/
│       ├── models/
│       └── services/
│
├── tests/
├── docs/
├── .github/
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore

🗺️ Roadmap
v0.1.0

Basic syntax validation

Initial project structure

Unit tests

v0.2.0

Domain validation

DNS / MX checks

v0.3.0

Disposable email detection

v0.4.0

SMTP verification

v0.5.0

CSV bulk validation

v1.0.0

Stable API

Documentation

Reports

Improved error handling

⚠️ Limitations

Email validation cannot guarantee that a mailbox actually exists.

Some mail servers intentionally prevent external verification, while others accept messages for any address on their domain.

For this reason, the validator reports whether an address is likely valid rather than guaranteeing that the mailbox exists.

🤝 Contributing

Contributions, suggestions and bug reports are welcome.

Feel free to open an issue or submit a pull request.


See the LICENSE file for more information.

Made with ❤️ for learning, experimentation and practical use.
