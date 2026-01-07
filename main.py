import os
import certifi
import smtplib
import ssl
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

load_dotenv()

EMAIL = os.environ["SMTP_USER_G"]
PASSWORD = os.environ["SMTP_PASSWORD_G"]

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

FROM_EMAIL = EMAIL
TO_EMAIL = "fleischer1@live.no"
SUBJECT = "Just a Test"

# Force Python to use certifi CA bundle
os.environ["SSL_CERT_FILE"] = certifi.where()

msg = MIMEMultipart()
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL
msg["Subject"] = SUBJECT

with open("message.txt", "r", encoding="utf-8") as f:
    msg.attach(MIMEText(f.read(), "plain", "utf-8"))

filename = "BC.jpg"
with open(filename, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
msg.attach(part)

context = ssl.create_default_context(cafile=certifi.where())

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(EMAIL, PASSWORD)
    server.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())

print("Sent!")
