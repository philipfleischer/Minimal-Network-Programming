# Minimal Networking Programming

### A collection of small networking experiments implemented in Python, focusing on low-level socket programming and secure communication.

## Encrypted Chat

### A minimal peer-to-peer encrypted chat application using TCP sockets and RSA public-key cryptography.

#### Features

• Direct peer-to-peer communication over TCP
• RSA key pair generation at runtime
• Public key exchange during connection setup
• End-to-end encrypted messages
• Concurrent send/receive using threads

#### Files

• encrypt_chat.py – Encrypted chat application (host or client)

#### How it works

• Each peer generates an RSA key pair (1024-bit)
• One peer hosts, the other connects
• Public keys are exchanged when the connection is established
• Messages are encrypted using the recipient’s public key
• Messages are decrypted locally using the private key

### Purpose

#### This project demonstrates:

• Secure communication concepts
• Public-key cryptography in practice
• Socket programming without frameworks
• Thread-based concurrency in networked applications

Note: This is an educational example and not intended for production use.
