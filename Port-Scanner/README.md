# Multithreaded TCP Port Scanner

A simple **Python** port scanner that checks for open **TCP ports** on a target host using multithreading.

The project demonstrates basic socket programming, concurrency, and port scanning techniques.

## Files

- Port-Scanner/portscanner.py – multithreaded TCP port scanner

## Overview

- Scans ports 1–1023 on a target host
- Uses TCP sockets (SOCK_STREAM)
- Performs concurrent scans using Python threads
- Collects and prints open ports

## How It Works

1. A queue is filled with port numbers to scan.
2. Multiple worker threads consume ports from the queue.
3. Each worker attempts a TCP connection to a port.
4. Successfully connected ports are reported as open.

## Running the Scanner

### Requirements

- Python 3.9+

Run the scanner:

```bash
python Port-Scanner/portscanner.py

Configuration
- Change the target host by modifying:

target = "127.0.0.1"

- Adjust scan range:

port_list = range(1, 1024)

- Adjust concurrency:

for t in range(300):
```

Notes

- This scanner uses a basic TCP connect scan (no stealth).
- High thread counts may stress the target or the local system.
- Intended for educational purposes and authorized testing only.
