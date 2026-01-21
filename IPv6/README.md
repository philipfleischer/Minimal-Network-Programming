# IPv6 TCP Client–Server Example

A minimal **Python** client–server application demonstrating **TCP communication over IPv6** using the built-in socket module.

## Files

- IPv6/server.py – IPv6 TCP server
- IPv6/client.py – IPv6 TCP client

## Overview

- Uses IPv6 sockets (AF_INET6)
- Communicates over TCP (SOCK_STREAM)
- Runs on the IPv6 loopback address (::1)
- Demonstrates basic send/receive message flow

## How It Works

1. The server binds to ::1 on port 9999 and listens for incoming connections.
2. The client connects to the server using IPv6.
3. The client sends a message to the server.
4. The server prints the message and responds.
5. The client receives and prints the server response.

## Running the Example

### Requirements

- Python 3.9+
- IPv6 support enabled on the system

### Start the server

```bash
python IPv6/server.py

Run the client (in a separate terminal)

python IPv6/client.py

Expected Output

Server:

Hello from client!

Client:

Hello from server!
```

Notes

- This example uses blocking sockets and handles one client at a time.
- The IPv6 loopback address (::1) restricts communication to the local machine.
- Intended as a minimal demonstration of IPv6 socket programming, not a production server.
