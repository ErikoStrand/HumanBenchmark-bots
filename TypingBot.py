import string
import cv2
import pytesseract
import keyboard
import pyautogui
import time
TYPING_DELAY = 0.05 # SET TO 0 AND SEE WHAT HAPPENS.
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
LEFT, TOP = 480, 395
RIGHT, BOTTOM = 1425, 550
img = pyautogui.screenshot("text.png", region=(LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP))
img = cv2.imread("text.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img)
list_of_words = text.split(" ")
print(list_of_words)
print("\n", "Newlist", "\n")
for i in range(len(list_of_words)):
    list_of_words[i]=list_of_words[i].replace('\n',' ')
string_text = " ".join(list_of_words)
print(string_text)
pyautogui.leftClick((480, 395))
keyboard.write(string_text, delay= TYPING_DELAY)