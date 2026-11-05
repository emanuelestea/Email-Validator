Email \& DNS Intelligence Tool



A Python-based tool designed to validate email addresses and analyze domain-related DNS information.



The project aims to explore email validation, DNS resolution, networking concepts, and defensive security through practical Python development.



Project status: In development 🚧



Current Features

Email Syntax Validation



The first implemented component provides email syntax validation using the email-validator library.



Current capabilities:



Validates email address syntax.

Normalizes email addresses.

Removes leading and trailing whitespace.

Handles empty and whitespace-only inputs.

Handles invalid data types.

Returns structured validation results.

Provides descriptive error messages.

Validation Scope



The current implementation checks email syntax only.



It does not currently verify:



Whether the email domain has valid DNS records.

Whether the recipient mailbox actually exists.

Whether the address can receive messages.



These capabilities are planned for future development.



Technology Stack

Python 3.10+

email-validator – Email syntax validation.

pytest – Automated testing.

Ruff – Code quality and formatting.

Project Structure

text

email-dns-intelligence/

│

├── src/

│   └── email\_intelligence/

│       └── validator.py

│

├── tests/

│   └── test\_validator.py

│

├── pyproject.toml

├── README.md

└── .gitignore



Installation



Clone the repository:



bash

git clone <repository-url>

cd email-dns-intelligence





Create a virtual environment:



bash

python -m venv .venv





Activate it on Windows:



powershell

.venv\\Scripts\\Activate.ps1





Install the project dependencies according to the project configuration.



Usage



Example:



python

from email\_intelligence.validator import validate\_email\_syntax



result = validate\_email\_syntax("mario@example.com")



print(result)





Example output:



python

{

&#x20;   "is\_valid": True,

&#x20;   "original": "mario@example.com",

&#x20;   "normalized": "mario@example.com",

&#x20;   "error": None

}



Running Tests



Run the test suite:



bash

python -m pytest -v





Run Ruff:



bash

ruff check .





Check code formatting:



bash

ruff format --check .



Development Roadmap



Planned features:



Email syntax validation.

Email normalization.

Input validation and error handling.

Unit tests for valid and invalid inputs.

DNS record analysis (MX, A, AAAA, TXT, NS).

DNS error and timeout handling.

Domain intelligence reporting.

SMTP analysis in authorized test environments.

REST API using FastAPI.

Command-line interface.

JSON reporting.

Docker support.

GitHub Actions CI pipeline.

Disclaimer



This project is developed for educational purposes.



All network-related tests and security assessments should be performed only on systems and infrastructure owned by the user or with explicit authorization.



Author



Developed as a personal Python, Networking, and Cybersecurity learning project.

