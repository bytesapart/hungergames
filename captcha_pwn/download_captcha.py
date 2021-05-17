import pyautogui
# print(pyautogui.position())
from time import sleep
print('Press Ctrl-C to quit.')
try:
    i = 0
    while i < 200:
        pyautogui.click(x=1120, y=-415, button='right')  # Right click on captcha
        sleep(1)
        pyautogui.click(x=1144, y=-376)  # Click on save image
        sleep(1)
        pyautogui.click(x=775, y=-575)  # Click save button
        sleep(2)
        pyautogui.click(x=1192, y=-396)  # Click on refresh image
        # pyautogui.click(x=1192, y=-374)  # Click on refresh image
        sleep(1)
        i += 1
        print(i)

except KeyboardInterrupt:
    print('\n')