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
_, msgnums = imap.search(None, "ALL")
# print(msgnums) -> [b'1 2 3 4']
for msgnum in msgnums[0].split():
    # Fetching the data in the emails:
    _, data = imap.fetch(msgnum, "(RFC822)")
    # print(data)
    message = email.message_from_bytes(data[0][1])  # Message object

    print(f"Message Number: {msgnum}")
    print(f"From: {message.get("From")}")
    print(f"To: {message.get("To")}")
    print(f"BCC: {message.get("BCC")}")
    print(f"Date: {message.get("Date")}")
    print(f"Subject: {message.get("Subject")}")
    print("Content:")
    for part in message.walk():  # Parts yielded by the walk() func
        if part.get_content_type() == "text/plain":
            print(part.as_string())

imap.close()
