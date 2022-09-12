import pyautogui
import time
import numpy as np
import mouse
import keyboard
ROUND = 1
CORDS = []
START = (915, 550)
LEFT, TOP = 762, 260
RIGHT, BOTTOM = 1141, 639
GRID_X, GRID_Y = 3, 3
GRID_SIZE = int((BOTTOM - TOP) / 3)
print(GRID_SIZE)
GAME = (LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP)

def click_mouse(x, y):
    mouse.move(x, y, absolute=True)
    time.sleep(0.2)
    mouse.click(button="left")
start_img = pyautogui.screenshot()
if start_img.getpixel(START) == (255, 209, 84):
    click_mouse(915, 550)
    time.sleep(0.01)     
print("start")

while keyboard.is_pressed("q") == False:
    click = False
    start = time.time()
    img = pyautogui.screenshot(region = GAME)
    for x in range(GRID_X):
        x = x * GRID_SIZE
        for y in range(GRID_Y):
            y = y * GRID_SIZE
            if img.getpixel((x + GRID_SIZE/2, y + GRID_SIZE/2)) == (255, 255, 255):
                if len(CORDS) > 0:
                    if [x + LEFT + GRID_SIZE/2, y + TOP + GRID_SIZE/2] != CORDS[-1]:
                        CORDS.append([x + LEFT + GRID_SIZE/2, y + TOP + GRID_SIZE/2])
                        click = True
                        break
                elif len(CORDS) <= 0:
                    CORDS.append([x + LEFT + GRID_SIZE/2, y + TOP + GRID_SIZE/2])
                    click = True
                    break
            if click: break
        if click: break

                    
    print(CORDS)
    while len(CORDS) == ROUND:
        time.sleep(1)
        for xy in CORDS:
            click_mouse(xy[0], xy[1])
            time.sleep(0.1)
        ROUND += 1
        CORDS = []
    #print(len(CORDS), "round;", ROUND)