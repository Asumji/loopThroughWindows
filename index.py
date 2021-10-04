import time
import pynput
import pydirectinput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

programPos = (-762, 1004)
windowArray = [(-1126, 909), (-969, 926), (-784, 921), (-549, 907), (-330, 876), (-120, 892)]
button = "space"

keyboard = Controller()
mouse = MouseController()
while True:
    time.sleep(600)
    for pos in windowArray:
        mouse.position = programPos
        time.sleep(0.1)
        mouse.click(Button.left)
        time.sleep(1)
        mouse.position = pos
        time.sleep(0.2)
        mouse.click(Button.left)
        time.sleep(0.2)
        pydirectinput.keyDown(button)
        time.sleep(0.5)
        pydirectinput.keyUp(button)
        time.sleep(1)
