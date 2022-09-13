import pyautogui
import time
import mouse

LEFT, TOP = 614, 307
RIGHT, BOTTOM = 860, 390
GAME = (LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP)
def click_mouse(x, y):
    mouse.move(x, y, absolute=True)
    mouse.click(button="left")
    time.sleep(0.2)
    
clicked = 0
while True:
    SCREEN = pyautogui.screenshot(region = GAME)
    if SCREEN.getpixel((20, 20)) == (43, 135, 209):
        click_mouse(714, 407)
    if SCREEN.getpixel((20, 20)) == (75, 219, 106):
        click_mouse(714, 407)
        clicked += 1
    if clicked == 5:
        break