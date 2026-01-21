# FTP Client (FTP / SFTP)

A simple Python script demonstrating file transfer using both **FTP** and **SFTP**.

The project highlights the difference between:

- traditional FTP (ftplib)
- secure SFTP over SSH (paramiko)

## Files

- FTP_Client/FTP_Client.py – main program (FTP and SFTP client)
- FTP_Client/myupload.txt – example file used for upload

## Functionality

### SFTP (Paramiko)

- Connects to an SFTP server over SSH
- Lists the contents of the home directory

### FTP (ftplib)

- Logs in to an FTP server
- Supports:
  - file download
  - file upload
  - changing directory and downloading a file

The operation is selected using the CHOICE constant:

- 1 – download file
- 2 – upload file
- 3 – change directory (cwd) and download file

The protocol is selected using the MODE constant:

```python
MODE = "SFTP"  # or "FTP"

Running the Program

Requirements
- Python 3.9+
- Paramiko (for SFTP)

Install dependencies:

pip install paramiko

Run the program:

python FTP_Client/FTP_Client.py

Notes
- Server addresses, usernames, and passwords are hardcoded for demonstration purposes.
- FTP transfers data in plaintext and should only be used in controlled test environments.
- SFTP uses encrypted SSH transport and is recommended in practice.

```
