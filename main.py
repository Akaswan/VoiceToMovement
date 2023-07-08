import pyautogui
from pynput.keyboard import Controller
import time
import pydirectinput

keyboard = Controller()

time.sleep(1)
keyboard.press('a')
time.sleep(2)
keyboard.release('a')
pyautogui.click()
keyboard.press('d')
time.sleep(2)
keyboard.release('d')
pydirectinput.moveTo(0, 0)