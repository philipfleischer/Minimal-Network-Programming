# Secure Login Client–Server (TCP)

A minimal **Python** client–server authentication system demonstrating **secure password handling** using hashing and a local database.

The project shows how a TCP server can authenticate users against stored, hashed credentials.

## Files

- Secure-Login/client.py – TCP client for login
- Secure-Login/server.py – multithreaded TCP authentication server
- Secure-Login/samples.py – initializes the user database with hashed passwords
- Secure-Login/userdata.db – SQLite database storing user credentials

## Overview

- Client connects to a TCP server and submits username and password
- Server hashes the received password using SHA-256
- Credentials are verified against a SQLite database
- Server responds with login success or failure
- Supports multiple concurrent clients using threads

## Security Features

- Passwords are never stored in plaintext
- SHA-256 hashing is used for password verification
- SQLite database used for credential storage

## Running the Project

### Requirements

- Python 3.9+

### Initialize the database

Run once to create and populate the database:

```bash
python Secure-Login/samples.py

Start the server

python Secure-Login/server.py

Run the client (in a separate terminal)

python Secure-Login/client.py
```

Notes

- This project demonstrates authentication concepts only and is not production-ready.
- No encryption is applied to the TCP connection itself.
- Intended for educational use to illustrate hashing, sockets, and basic authentication logic.
