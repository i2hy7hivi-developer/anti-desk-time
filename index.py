import time
import random

try:
    import pyautogui
    x, y = pyautogui.position()
    screen_width, screen_height = pyautogui.size()
    try:
        while True:
            i = random.randint(1, screen_width)
            j = random.randint(1, screen_height)
            pyautogui.moveTo(i, j)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user.")
except ImportError:
    print("pyautogui is not installed.")