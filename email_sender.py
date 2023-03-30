# Email Sender

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'rishirsavla@gmail.com'
email_password = 'rishi3566'

email_receiver = 'rishirsavla@gmail.com'

subject = "Don't forget to visit our website"

body = """
To learn more about data science please visit our website and explore.

Thank You!
"""

e = EmailMessage()
e['From'] = email_sender
e['To'] = email_receiver
e['subject'] = subject
e.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',500,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.login(email_sender,email_receiver, e.as_string())




