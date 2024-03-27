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

# MIME TYPE 
# msg.add_attachment()
with open('myw3schoolsimage.jpg', 'rb') as f:
    msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename=f.name)

with open('test.pdf', 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=f.name)



with smtplib.SMTP ("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)