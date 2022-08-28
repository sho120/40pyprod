import pyautogui
import time
import pyperclip

weather = ["서울 날씨", "일산 날씨", "부산 날씨", "평택 날씨", "송도 날씨"]

addr_x=150
addr_y=50

start_x = 404
start_y = 350
end_x = 1047
end_y = 650

for each_weather in weather:
    pyautogui.moveTo(addr_x, addr_y,1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com",interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(each_weather)
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)

    pyautogui.write(["enter"])
    time.sleep(1)

    path = 'Chapter4\main10\\' + each_weather + '.png'
    pyautogui.screenshot(path, region=(start_x,start_y,end_x-start_x,end_y-start_y))