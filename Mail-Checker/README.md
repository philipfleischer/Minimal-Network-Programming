# IMAP Mail Checker

A simple **Python** script that connects to an email account using **IMAP over SSL/TLS** and reads messages from the inbox.

The project demonstrates basic email retrieval and parsing using Python’s standard libraries.

## Files

- Mail-Checker/mail_checker.py – IMAP email reader script

## Overview

- Connects securely to an IMAP server (imap.gmail.com)
- Authenticates the user at runtime
- Selects the inbox mailbox
- Iterates through all messages and prints metadata and content

## Features

- Secure IMAP connection (IMAP4_SSL)
- Runtime password input (no hardcoded credentials)
- Displays:
  - Sender
  - Recipient
  - BCC
  - Date
  - Subject
  - Plain text message body

## Running the Script

### Requirements

- Python 3.9+
- An email account with IMAP access enabled

Run the script:

```bash
python Mail-Checker/mail_checker.py
```

You will be prompted to enter your email password at runtime.

Notes

- Gmail typically requires an app-specific password for IMAP access.
- Only text/plain parts of multipart emails are printed.
- This script is intended for educational purposes and does not modify or delete emails.
