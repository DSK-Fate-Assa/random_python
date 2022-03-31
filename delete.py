import pyautogui as pow
import time
import random
import tkinter as tk
import rotatescreen as rt
import os 
os.system('pip install pyautogui --user')
os.system('pip install rotate-screen --user')
screen = rt.get_primary_display()

root = tk.Tk()

wid = root.winfo_screenwidth()
hei = root.winfo_screenheight()
eegoo = pow.leftClick
pow.FAILSAFE = False

while True:
    pow.moveRel(random.randint(wid/2 - wid, wid/2), random.randint(wid/2 - hei, hei/2))
    eegoo()
    time.sleep(0.00015)
    screen.rotate_to(random.choice([90*i for i in range(4)]))
    time.sleep(0.5)