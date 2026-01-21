# GUI SMTP Mail Client

A simple email client with a graphical user interface built in **Python** using **PySide6**.
The application connects to an SMTP server using **STARTTLS**, allowing the user to compose emails, attach files, and send messages.

## Files

- `GUI_SMTP/mail_GUI_client.py` – application logic (GUI + SMTP)
- `GUI_SMTP/mail_gui_client.ui` – Qt Designer UI file

## Features

- Login to an SMTP server (server + port)
- TLS-encrypted authentication (`starttls`)
- Compose emails with recipient, subject, and message body
- Attach one or more files
- Basic error handling and user confirmation before sending

## Running the Application

### Requirements

- Python 3.9+
- PySide6

Install dependencies:

```bash
pip install PySide6

Run the application (from GUI_SMTP/):

python mail_GUI_client.py
```

The program expects mail_gui_client.ui to be located in the same directory as the Python file.

Notes

- SMTP login requires valid server details and credentials.
- Many email providers require app-specific passwords for SMTP access.
- This project is intended as a simple demonstration of GUI-based networking programming.
