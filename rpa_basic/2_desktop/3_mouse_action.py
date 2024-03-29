import pyautogui as pg

# pg.sleep(3)  # 3초 대기
# print(pyautogui.position())

# pyautogui.click(40,161, duration=1) # 1초 동안 이동해서 마우스 클릭

#.click() 은 아래 두개를 합친 것
# pg.mouseDown()
# pg.mouseUp()

# pg.doubleClick()
# pg.click(clicks=500)

# pg.moveTo(500, 500)
# pg.mouseDown()
# pg.moveTo(600,600)
# pg.mouseUp()

pg.sleep(3)
# pg.rightClick()
# pg.middleClick()

# print(pg.position())
# pg.moveTo()
# # pg.drag(100, 0) # 현재 위치를 기준으로 x 100 만큼, y 0 만큼 드래그
# pg.drag(100, 0, duration=0.25)  # 너무 빠른 동작으로 drag 수행이 안 될 때는 duration 옵션 추가
# pg.dragTo(1514, 137) # 절대 좌표 기준으로 x 1514, y 349로 드래그

pg.scroll(300) # 양수면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤

