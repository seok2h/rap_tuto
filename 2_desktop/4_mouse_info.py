import pyautogui as pg
# pg.FAILSAFE = false # 귀퉁이에서 머물고 있으면 프로그램을 자동으로 꺼버림
# pg.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pg.mouseInfo()

for i in range(10):
    pg.move(100, 100)
    # pg.sleep(1)
