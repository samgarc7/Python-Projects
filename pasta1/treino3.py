import pyautogui as py
import webbrowser
import time 
time.sleep(1)
webbrowser.open("https://www.google.com")
time.sleep(2)
py.write("netflix")
time.sleep(1)
py.press("enter")
