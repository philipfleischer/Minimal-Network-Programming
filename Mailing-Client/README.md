# SMTP Mailing Client

A simple **Python** mailing client that sends an email via **SMTP with STARTTLS**, including a text message and a file attachment.
The project demonstrates secure email delivery using environment variables and TLS.

## Files

- Mailing-Client/main.py – SMTP mail sender
- Mailing-Client/message.txt – email body content
- Mailing-Client/BC.jpg – example attachment
- Mailing-Client/.env – environment variables (not committed)
- Mailing-Client/.gitignore – excludes sensitive files

## Features

- Secure SMTP connection using STARTTLS
- Credentials loaded from environment variables
- Explicit TLS certificate handling using certifi
- Supports UTF-8 text and binary file attachments
- Debug output enabled for SMTP session

## Running the Client

### Requirements

- Python 3.9+
- python-dotenv
- certifi

Install dependencies:

```bash
pip install python-dotenv certifi

Setup

Create a .env file in Mailing-Client/:

SMTP_USER_G=your_email@gmail.com
SMTP_PASSWORD_G=your_app_password

Run

python Mailing-Client/main.py
```

Notes

- Gmail requires an app-specific password for SMTP access.
- The .env file should never be committed to version control.
- This project is intended as a minimal demonstration of secure SMTP email sending in Python.
