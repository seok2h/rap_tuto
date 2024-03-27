import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='./4_email/.env')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_ADDRESS2 = os.getenv('EMAIL_ADDRESS2')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = "테스트 메일입니다"
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS2

# 여러 명에게 메일을 보낼 때
# msg['To'] = 'a@a', 'b@b'
# to_list = ['a@a', 'b@b']
# msg['To'] = ", ".join(to_list)

msg.set_content("테스트 본문입니다")

with smtplib.SMTP ("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)