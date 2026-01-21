# Minimal Python HTTP Server

A minimal HTTP server implemented in **Python** using the built-in http.server module.
The server demonstrates basic handling of **GET** and **POST** requests without external frameworks.

## Overview

- Serves a simple HTML response on GET
- Returns the current server timestamp as JSON on POST
- Binds explicitly to a local IP address and port

## Files

- http_server.py – minimal HTTP server implementation

## Functionality

- **GET /**
  Returns a simple HTML page:

  ```html
  <html>
    <body>
      Hello World!
    </body>
  </html>
  ```

- POST /
  Returns the current server time in JSON format:

{ "time": "YYYY-MM-DD HH:MM:SS" }

Running the Server

Requirements

- Python 3.9+

Start the server

python http_server.py

The server listens on:

http://192.168.1.11:8000

Testing

Test with a browser:

http://192.168.1.11:8000

Test with curl:

curl http://192.168.1.11:8000
curl -X POST http://192.168.1.11:8000

Notes

- The server is single-threaded and intended for demonstration purposes only.
- No routing, persistence, or security mechanisms are implemented.
- Binding to a specific IP allows access from other devices on the same local network.
