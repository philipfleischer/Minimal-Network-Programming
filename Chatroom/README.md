Minimal Networking Programming

A collection of small networking experiments implemented in Python, focusing on low-level socket programming and concurrency.

Chatroom Project

A simple TCP-based chat application using Python sockets and threads.

Features
• Client–server architecture over TCP
• Multiple concurrent clients using threading
• Nickname-based chat
• Admin user with special commands:
• /kick <username> – remove a user from the chat
• /ban <username> – ban a user permanently
• Persistent ban list stored in bans.txt

Files
• server.py – Chat server handling connections, broadcasting messages, and admin commands
• client.py – Chat client for sending and receiving messages
• bans.txt – Persistent list of banned nicknames (initially empty)

How it works
• The server listens on 127.0.0.1:55554
• Clients connect, choose a nickname, and can chat in real time
• The nickname admin requires a password and has moderation privileges
• All communication is done using raw TCP sockets

Purpose

This project is intended as a minimal, educational example of:
• Socket programming
• Thread-based concurrency
• Basic application-level protocols
• Simple server-side state management

⸻
