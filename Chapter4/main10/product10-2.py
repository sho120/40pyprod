import pyautogui
import time
import pyperclip

pyautogui.moveTo(700,235,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 404
start_y = 350
end_x = 1047
end_y = 650

pyautogui.screenshot(r'Chapter4\main10\seoulWether.png', region=(start_x,start_y,end_x-start_x,end_y-start_y))