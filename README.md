# Minimal-Networking-Programming

A curated collection of **small, focused networking projects implemented in Python**, showcasing practical experience with
socket programming, application-layer protocols, security, concurrency, and basic backend development.

This repository is designed as a **portfolio showcase**, where each project isolates one or two core networking concepts and implements them in a minimal, readable, and educational way.

---

## Project Overview

| Project        | Description                                                                       | Links                     |
| -------------- | --------------------------------------------------------------------------------- | ------------------------- |
| GUI_SMTP       | GUI-based SMTP email client with STARTTLS and file attachments (PySide6)          | [Files](./GUI_SMTP)       |
| FTP_Client     | FTP and SFTP client demonstrating plaintext vs encrypted file transfer            | [Files](./FTP_Client)     |
| HTTP-Server    | Minimal Python HTTP server handling GET and POST requests                         | [Files](./HTTP-Server)    |
| IPv6           | IPv6 TCP client–server example using Python sockets                               | [Files](./IPv6)           |
| Mail-Checker   | IMAP client for reading and parsing emails securely                               | [Files](./Mail-Checker)   |
| Mailing-Client | Secure SMTP mailing client using STARTTLS, environment variables, and attachments | [Files](./Mailing-Client) |
| Port-Scanner   | Multithreaded TCP port scanner                                                    | [Files](./Port-Scanner)   |
| Secure-Login   | TCP-based login system with hashed passwords and SQLite                           | [Files](./Secure-Login)   |
| Chatroom       | TCP-based multi-client chat server with admin commands and persistent bans        | [Files](./Chatroom)       |
| Encrypted-Chat | Peer-to-peer encrypted chat using TCP sockets and RSA cryptography                | [Files](./Encrypted-Chat) |
| FLASK_REST_API | RESTful API built with Flask for managing a simple video catalogue                | [Files](./FLASK_REST_API) |

---

## Key Topics Covered

- TCP/IP socket programming (IPv4 & IPv6)
- Application-layer protocols: HTTP, SMTP, IMAP, FTP, SFTP
- Secure communication (TLS, STARTTLS, SSH, RSA)
- Authentication and password hashing
- Multithreading and concurrency
- Client–server and peer-to-peer architectures
- Basic REST API and backend concepts

---

## Technologies & Tools

- Python 3
- Standard libraries: socket, threading, queue, ssl, hashlib, sqlite3
- Networking libraries: smtplib, imaplib, ftplib, paramiko
- Web framework: Flask, Flask-RESTful
- GUI: PySide6
- Cryptography: RSA (educational use)

---

## Purpose

This repository is intended for:

- Demonstrating hands-on networking knowledge
- Showcasing protocol-level understanding without heavy frameworks
- Serving as a **portfolio and CV reference**

Each project is intentionally kept **small and focused** to emphasize clarity, correctness, and core concepts over production complexity.
