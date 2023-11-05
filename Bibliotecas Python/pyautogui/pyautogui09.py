import pyautogui as auto

from time import sleep as s



s(3)
auto.hotkey('Ctrl','b')
s(5)
auto.hotkey('Ctrl','4')
s(6)
auto.moveTo(450,279)
auto.click(450,279)
s(4)
auto.write('#BBB23')