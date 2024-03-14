"""
아래 동작을 자동으로 수행하는 프로그램을 작성하시오

1. 그림판 실행 (단축기 : win + r, 입력값 : mspaint) 및 최대화

2. 상단의 텍스트 기능을 이용해서 흰 영역 아무 곳에다가 글자 입력
    - 입력 글자 : "참 잘했어요"

3. 5초 대기 후 그림판 종료
    이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함
"""

import pyautogui as pg
import os

pg.hotkey('win', 'r', interval=0.2)
pg.write("mspaint")

pg.press('enter', interval=0.1)

pg.sleep(0.5)
w = pg.getActiveWindow()
w.maximize()

pg.sleep(1)
write_icon_location = pg.locateOnScreen('write_icon.png', confidence=0.9)
pg.click(write_icon_location)
pg.move(700, 300)
pg.sleep(1.5)
pg.click(clicks=2)

import pyperclip
pyperclip.copy("참 잘했어요")
pg.hotkey('ctrl', 'v')

pg.sleep(5)

w.close()

# pg.click(pg.locateOnScreen('no_save.png', confidence=0.9))

print("끝")






