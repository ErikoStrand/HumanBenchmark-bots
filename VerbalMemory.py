import mouse
import cv2
import pytesseract
import pyautogui
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
def click_mouse(x, y):
    mouse.move(x, y, absolute=True)
    time.sleep(0.2)
    mouse.click(button="left")
LEFT, TOP = 400, 380
RIGHT, BOTTOM = 1400, 450
NEW_BOTTON = [1020, 500]
SEEN_BOTTON = [880, 500]
SEEN = []

    
time.sleep(1)
while keyboard.is_pressed("q") == False:
    time.sleep(0.2)
    img = pyautogui.screenshot("text.png", region=(LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP))
    img = cv2.imread("text.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    
    if list[text] in SEEN:
        click_mouse(SEEN_BOTTON[0], SEEN_BOTTON[1])
        print("seen", SEEN, text)
        
    if list[text] not in SEEN:
        click_mouse(NEW_BOTTON[0], NEW_BOTTON[1])
        SEEN.append(list[text])
        print("new", SEEN, text)
        
    