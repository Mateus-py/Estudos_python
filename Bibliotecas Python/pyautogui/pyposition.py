import pyautogui

from time import sleep


p = str(input('Ir para o loop ou ver keys disponiveis? [L] - [K] #BBB23l')).upper()


if p == 'L':
    loop = True
    while loop == True:
        sleep(1)
        print(pyautogui.position())
if p == 'K':
    keys = pyautogui.KEYBOARD_KEYS

    print(keys)