import pyautogui

n=input()

pyautogui.moveTo(91,25)
pyautogui.click()
pyautogui.moveTo(130,828)
pyautogui.sleep(1)
pyautogui.write(n)
pyautogui.press("enter")
