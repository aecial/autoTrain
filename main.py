import pyautogui
import time

try: 
    while True:
        pyautogui.moveTo(200, 300)

        pyautogui.moveRel(100, 150)
        pyautogui.click()
        pyautogui.press('space')
        time.sleep(10)
except KeyboardInterrupt:
    print('Stopped')
 