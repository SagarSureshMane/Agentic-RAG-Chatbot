from langchain_core.tools import tool
from email.mime.text import MIMEText

import smtplib
import os


@tool
def send_email(
    recipient: str,
    subject: str,
    body: str
) -> str:
    """
    Send an email using SMTP.
    """

    try:
        sender = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_PASSWORD")

        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        server = smtplib.SMTP(
            os.getenv("SMTP_SERVER"),
            int(os.getenv("SMTP_PORT"))
        )

        server.starttls()

        server.login(
            sender,
            password
        )

        server.send_message(msg)

        server.quit()

        return "Email sent successfully"

    except Exception as e:
        return f"Email error: {str(e)}"