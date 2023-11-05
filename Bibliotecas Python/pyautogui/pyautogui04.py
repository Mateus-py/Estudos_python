import pyautogui as auto

auto.PAUSE = 3

posquickshare = ('187','334')
poschat = ('770','695')

auto.hotkey('Ctrl','b')
auto.hotkey('Ctrl','2')
auto.moveTo(posquickshare)
auto.click(posquickshare)
auto.moveTo(poschat)
auto.click(poschat)
for i in range(0,3):
    auto.write('OI')
