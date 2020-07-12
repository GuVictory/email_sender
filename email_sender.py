import smtplib
from email.message import EmailMessage
import os
from pipenv.vendor.dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


EMAIL_LOGIN = os.getenv("email_login")
EMAIL_PASSWORD = os.getenv("email_password")


email = EmailMessage()
email['from'] = 'Python Creeeper'
email['to'] = 'gubanova.vi10@gmail.com'
email['subject'] = 'Super secret msg'

email.set_content('Haha, Hello, World!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    smtp.send_message(email)
    print('Message was send!')
