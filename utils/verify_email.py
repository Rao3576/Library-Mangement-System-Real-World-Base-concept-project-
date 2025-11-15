# app/email_utils.py
import smtplib
from email.mime.text import MIMEText
from config.config import settings

'''def send_verification_email(email: str, token: str):
    msg = MIMEText(f"Click to verify your email: http://localhost:8000/user/verify-email?token={token}")
    msg['Subject'] = "Verify your email"
    msg['From'] = settings.SMTP_EMAIL
    msg['To'] = email

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_EMAIL, email, msg.as_string())'''


def send_verification_email(email: str, token: str):
    smtp_email = "kashifmushtaquaf@gmail.com"
    smtp_password = "zpfrzblhkszirhuh"  # your app password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEText(f"Click to verify your email: http://localhost:8000/user/verify-email?token={token}")
    msg['Subject'] = "Verify your email"
    msg['From'] = smtp_email
    msg['To'] = email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_email,smtp_password)
            server.sendmail(smtp_email, email, msg.as_string())
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication failed: {e}")
        raise
