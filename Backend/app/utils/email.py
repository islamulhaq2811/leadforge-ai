import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)

SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_FROM = os.getenv("SMTP_FROM", SMTP_USER)
NOTIFY_EMAIL = os.getenv("NOTIFY_EMAIL", "")

def is_configured() -> bool:
    return bool(SMTP_HOST and SMTP_USER and SMTP_PASS and NOTIFY_EMAIL)

async def send_contact_notification(name: str, email: str, project_type: str, message: str) -> bool:
    if not is_configured():
        logger.warning("Email not configured — SMTP_HOST, SMTP_USER, SMTP_PASS, NOTIFY_EMAIL env vars required")
        return False

    subject = f"New Contact from {name} — {project_type}"
    body = f"""
New project inquiry from LeadForge AI website:

Name: {name}
Email: {email}
Project Type: {project_type}
Message: {message}
"""

    msg = MIMEMultipart()
    msg["From"] = SMTP_FROM
    msg["To"] = NOTIFY_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=15) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        logger.info(f"Contact email sent for {name} <{email}>")
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False
