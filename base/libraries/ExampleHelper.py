from time import sleep
import keyboard
import pyautogui


def tiempo_espera():
    sleep(5)


def press_enter():
        keyboard.press_and_release('enter')

def scroll():
	pyautogui.scroll(-500)

