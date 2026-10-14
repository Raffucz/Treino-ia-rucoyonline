import pyautogui as pg
import time
import keyboard

while True:
    time.sleep(1)
    print("Current mouse position:")
    pg.position()
    print(pg.position())
    time.sleep(0.5)

    if keyboard.is_pressed('q'):  # Pressione 'q' para sair do loop
        break