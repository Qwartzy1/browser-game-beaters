# Perfect Circle Drawer

import time
import pyautogui
import math

# time.sleep(3)
#
# radius = 360
# center_x = 1440
# center_y = 900

# This offsets the bookmarks tab because the center of the circle will change as well
# center_y += 34

# pyautogui.moveTo(center_x-radius,center_y)
# step = radius*2/20
#
# pyautogui.mouseDown()
# for i in range(0,int(radius*2/step)+1):
#     x = center_x-radius+i*step
#     y = math.sqrt(radius**2-(x-center_x)**2)+center_y
#     pyautogui.moveTo(x, y)
#
# for i in reversed(range(0,int(radius*2/step)+1)):
#     x = center_x-radius+i*step
#     y = -math.sqrt(radius**2-(x-center_x)**2)+center_y
#     pyautogui.moveTo(x, y)
#
# pyautogui.mouseUp()