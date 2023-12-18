import pyautogui as pa
import time
pa.PAUSE = 1


pa.press('win')
pa.write('chrome')
pa.press('ENTER')
pa.write('www.linkedin.com/in/murilorosacastro')
pa.press('ENTER')
time.sleep(4)
pa.rightClick(x=2649, y=552)
time.sleep(2)
pa.click(x=2708, y=334)

