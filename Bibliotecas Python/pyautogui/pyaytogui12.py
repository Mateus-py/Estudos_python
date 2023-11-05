import pyautogui as auto
from time import sleep as s


auto.hotkey('Ctrl','n')
s(5)
auto.write('inf = ')
s(3)
for i in range(0,100):
    auto.write('10*')

auto.press('enter')
auto.write('print(inf)')