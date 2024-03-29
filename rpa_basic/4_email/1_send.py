import smtplib
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='./4_email/.env')

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls()     # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)   # 로그인

    subject = "test mail" # 메익 제목
    body = "mail body"  # 메일 본문

    msg = f"Subject: {subject}\n{body}"

     # 발신자 수신자 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)