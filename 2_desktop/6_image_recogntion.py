import pyautogui as pg
import time

# file_menu = pg.locateOnScreen("file_menu.png")  # 화면에서 그림과 같은 부분을 찾아준다.
# print(file_menu)
# pg.click(file_menu)

# trash_icon = pg.locateOnScreen('run_icon.png')
# pg.moveTo(trash_icon)

# screen = pg.locateOnScreen("screenshot.png")
# print(screen)   # None 출력

# for i in pg.locateAllOnScreen("checkbox.png"):    # 화면에서 모두다 찾아라
#     print(i)
#     pg.click(i, duration=0.25)

# checkbox = pg.locateOnScreen("checkbox.png")
# pg.click(checkbox)  # 첫번째로 발견되는

# start = time.time()
# trash_icon = pg.locateOnScreen("trash_icon.png")
# pg.moveTo(trash_icon)
# end = time.time()
# print(f"{end - start:.5f} sec")

# 속도 개선
# 1. GrayScale
# start = time.time()
# trash_icon = pg.locateOnScreen("trash_icon.png", grayscale=True)
# pg.moveTo(trash_icon)
# end = time.time()
# print(f"{end - start:.5f} sec")

# 2. 범위 지정
# trash_icon = pg.locateOnScreen("trash_icon.png", region=(x, y, width, height)) # 설정한 범위 내에서 이미지를 찾아줌
# pg.moveTo(trash_icon)

# 3 정확도 조정
# run_btn = pg.locateOnScreen("run_icon.png", confidence=0.1)
# print(run_btn)
# pg.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pg.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pg.click(file_menu_notepad)
# else:
#     print("발견 실패")

# while file_menu_notepad is None:
#     file_menu_notepad = pg.locateOnScreen("file_menu_notepad.png")

# pg.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10
# start = time.time()
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pg.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit()

# pg.click(file_menu_notepad)

# def find_target(img+file, timeout=30):
#     start = time.time()
#     target = None
#     while target is None:
#         target = pg.locateOnScreen(img_file)
#         end = time.time()
#         if end - start > timeout:
#             break
#     return target

# def my_click(img_file, timeout=30):
#     target = find_target(img_file, timeout)
#     if target:
#         pg.click(target)
#     else:
#         print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program")
#         sys.exit()
        
# my_click("file_menu_notepad.png", 10)