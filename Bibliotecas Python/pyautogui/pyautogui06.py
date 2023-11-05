import pyautogui as auto
from time import sleep as s



s(2)
auto.press('win')
s(2)
auto.write('whats')
auto.press('Enter')
s(32)
auto.moveTo(151,195)
s(2)
auto.click(151,195)
s(2)
auto.moveTo(727,702)
auto.click(727,702)
for i in range(0,100):
    auto.write('OI')
    auto.press('Enter')