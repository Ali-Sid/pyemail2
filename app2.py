from email.message import EmailMessage
import ssl
import smtplib

email_sender = "xyz@gmail.com"
email_password = "123123"
email_receiver = "hello@saasedup.com"

subject = "This is another test email"
body = """
So, this is another test email with a diferent code in python, so enjoy reading this email and subscribe to my substack newsletter: https://alisid.substack.com
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    smtp.sendmail(email_sender, email_receiver, em.as_string())
