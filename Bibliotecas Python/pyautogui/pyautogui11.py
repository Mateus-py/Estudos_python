import pyautogui as auto

auto.PAUSE = 1

auto.hotkey('Ctrl','n')
auto.moveTo(208,178)
auto.doubleClick(208,178)

for c in range(0,100):
    auto.write('Ola,Mundo !!')