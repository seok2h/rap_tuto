# [신청 메일 양식]
# 제목 : 파이썬 특강 신청하빈다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#   (예) 나도코딩/1234

import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from random import *

nicknames = ["유재석", "박명수", "정현돈", "노홍철", "조세호"]

load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        # content = nickname + "/" + str(randint(1000, 9999))
        content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 my 계정으로 메일 발송 완료")
