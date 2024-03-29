import pyautogui as pg

# 스크린샷 찍기
# img = pg.screenshot()
# img.save("screenshot.png")  # 파일로 저장

pg.mouseInfo()

pixel = pg.pixel(28, 18)    # 해당 좌표의 픽셀을 가져옴
print(pixel)    # 해당 픽셀의 rgb를 튜플 형태로 출력해 줌

# print(pg.pixelMatchesColor(28, 18, (34, 167, 242))) # 앞에 좌표와 뒤의 rgb가 일치하는지 검사
# print(pg.pixelMatchesColor(28, 18, pixel))   # 위 명령어와 같은 명령어
# print(pg.pixelMatchesColor(28, 18, (34, 167, 243))) # 앞에 좌표와 뒤의 rgb가 일치하는지 검사


