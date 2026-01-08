import imaplib
import email
import getpass

# GMAIL IMAP server settings: imap.gmail.com port: 993 SSL/TLS

imap_server = "imap.gmail.com"
email_address = "philipfleischer45@gmail.com"
password = getpass.getpass("Write password: ")

imap = imaplib.IMAP4_SSL(imap_server)
# Now we are connected to the server and it is asking for credentials
imap.login(email_address, password)

# Select mailbox:
imap.select("Inbox")

# Iterate over messages in "Inbox"
