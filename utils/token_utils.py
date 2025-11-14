from datetime import datetime, timedelta
from jose import jwt, JWTError
from config.config import settings
from passlib.context import CryptContext
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_reset_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_reset_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None

def verify_email_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None


# utils/auth_user.py



def send_email(to_email: str, email_type: str, link: str):
    """
    Sends a verification or password reset email.
    email_type can be 'verify' or 'reset'.
    """
    subject = ""
    body = ""

    if email_type == "verify":
        subject = "Verify your account"
        body = f"Click the link below to verify your email:\n\n{link}\n\nIf you didn't request this, ignore this email."
    elif email_type == "reset":
        subject = "Reset your password"
        body = f"Click the link below to reset your password:\n\n{link}\n\nIf you didn't request this, ignore this email."
    else:
        raise ValueError("Invalid email type")

    message = MIMEMultipart()
    message["From"] = settings.SMTP_EMAIL
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
            server.send_message(message)
        print(f"✅ Email sent successfully to {to_email}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")






# def hash_password(password: str) -> str:
#     """Hashes a plain password using bcrypt."""
#     return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     """Verifies a password against its hash."""
#     return pwd_context.verify(plain_password, hashed_password)
