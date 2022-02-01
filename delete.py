import pyautogui as pow
import time

eegoo = pow.leftClick

while True:
    pow.moveRel(200, 60)
    eegoo()
    time.sleep(0.00015)
    pow.moveRel(100, -320)
    eegoo()
    time.sleep(0.00015)
    pow.moveRel(-150, 480)
    eegoo()
    time.sleep(0.00015)
    pow.moveRel(75, -300)
    eegoo()
    time.sleep(0.00015)
    pow.moveRel(175, -200)
    eegoo()
    time.sleep(0.00015)
    pow.moveRel(-400, 280)
    eegoo()
    time.sleep(0.00015)