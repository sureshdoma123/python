import pyautogui
import time

n=input("Enter time :")
##pyautogui.sleep(5)
##pyautogui.moveTo(336,72)
##pyautogui.click()
t=time.strftime("%H:%M:%S")
while 1:
    if t==n:
        pyautogui.moveTo(646,26)
        pyautogui.sleep(1)
        pyautogui.click()
        pyautogui.sleep(5)
        pyautogui.write("youtube.com")
        pyautogui.sleep(2)
        pyautogui.press("enter")#youtube.com
        break
    else:
        pyautogui.sleep(1)

    
        


