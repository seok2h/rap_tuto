from imap_tools import MailBox
from dotenv import load_dotenv
import os

load_dotenv("./4_email/.env")

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# with을 사용하면 mailbox.logout() 안해도 된다.
with MailBox("imap.gmail.com").login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch():     # 전체 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(UNSEEN)'):     # 읽지 않은 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(FROM a@gmail.com)', limit=3, reverse=True):     # 특정인이 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸야한다.
    # for msg in mailbox.fetch('(TEXT "test mail")', limit=3, reverse=True):     # 어떤 글자를 포함하는 메일 (제목, 본문)
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SUBJECT "test mail")', limit=3, reverse=True):     # 어떤 글자를 포함하는 메일 (제목만)
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch(limit=5, reverse=True):     # 한글은 조건문을 통한 필터링이 필요
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5):     # 특정 날짜 이후의 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일 (한 칸 띄우고 적으면 됨) (그리고 조건)
    # for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail")', reverse=True, limit=5):     # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건 중 하나라도 만족하는 메일 (또는 조건)
    # for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail)', reverse=True, limit=5):     # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
