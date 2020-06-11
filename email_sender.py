import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('EMAIL_USER') # enter server email here
password = os.getenv('EMAIL_PASSWORD') # enter password here

# give random integers for given length
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# send emails with verification code
def verification_key_passer(receiver_email, username):
    message = MIMEMultipart("alternative")
    message["Subject"] = "psichatbotsep"
    message["From"] = sender_email
    message["To"] = receiver_email

    code = random_with_N_digits(6)
    # Create the plain-text of message
    text = """Hi """ + username+ """,
    We must have your permission before doing transactions via the Chatbot service.
    Here is the Verification code : """+ str(code)+"""
        
    
    
    Thank you,
    Public service Inquiry System Team"""

    part1 = MIMEText(text, "plain")  # Turn these into plain MIMEText objects
    message.attach(part1)  # Add plain-text part to MIMEMultipart message

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return code

    

