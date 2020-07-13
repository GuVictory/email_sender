import smtplib
from email.message import EmailMessage
from os import getenv
from pipenv.vendor.dotenv import load_dotenv, find_dotenv
from string import Template
from pathlib import Path

load_dotenv(find_dotenv())

html = Template(Path('index.html').read_text())
EMAIL_LOGIN = getenv("email_login")
EMAIL_PASSWORD = getenv("email_password")


email = EmailMessage()
email['from'] = 'Python Creeeper'
email['to'] = 'email_to_send@gmail.com'
email['subject'] = 'Super secret msg'

email.set_content(html.substitute(name='Кит кит кашалот'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # The login and password from the mail is stored in .env file
    smtp.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    smtp.send_message(email)
    print('Message was send!')
