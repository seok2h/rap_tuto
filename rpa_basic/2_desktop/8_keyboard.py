import pyautogui as pg

# w = pg.getWindowsWithTitle("제목 없음")[0]
# print(w)
# w.activate()
# w.restore()

# pg.write("12345")
# pg.write("ABCDE", interval=0.25)

# pg.write(['t', 'e', 's', 't', 'left', 'left', 'right', 'l', 'a', 'enter'], interval=0.25)
# # t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력

# 특수 문자
# shift 4 -> $
# pg.keyDown("shift")
# pg.press("4")
# pg.keyUp("shift")

# 조합 키 (Hot Key)
# pg.keyDown("ctrl")
# pg.keyDonw('a')
# pg.keyUp('a')   # press('a')
# pg.keyUp('ctrl')

# 간편한 조합키
# pg.hotkey('ctrl', 'alt', 'shift' 'a')
# Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > ... > Ctrl 떼고

# import pyperclip
# pyperclip.copy("안녕하세요")    # 안녕하세요 글자를 클리보드에 저장
# pg.hotkey('ctrl', 'v')  # 클립보드에 잇는 내용을 붙여넣기  -> 한글 입력하는 방법

# def my_wrtie(text):
#     pg.copy(text)
#     pg.hotkey('ctrl', 'v')

# my_write("안녕하세요")

# win : ctrl + alt + del
# mac : cmd + shift + option + q

