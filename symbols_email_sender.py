import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

def setup_smtp_server():
    load_dotenv()  # take environment variables from .env.

    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(smtp_user, smtp_password)

    return server

def send_email(server, subject, to_email, content):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = server.login
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add in the message body
    msg.attach(MIMEText(content, 'plain'))

    # Send the email
    server.sendmail(server.login, to_email, msg.as_string())

def main():
    # Setup the server
    server = setup_smtp_server()

    # Send an email
    subject = "Test Email"
    to_email = "recipient@example.com"
    content = "Hello, this is a test email."

    send_email(server, subject, to_email, content)

    # After sending email, always close the server connection
    server.quit()

if __name__ == "__main__":
    main()