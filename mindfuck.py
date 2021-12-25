import sys
import time
import random
from colorama import init, Fore, Style, Back
init(autoreset=True)


def Error(text: str):
    print(text)
    input('Click enter to exit from a program...')
    exit()


def AnimationPrinting(text: str, secs: int):
    for symbol in text:
        print(symbol, flush=True, end="")
        time.sleep(secs)
    print("")


slots = []
special = ""
cursor_position = 1
for i in range(0, 5001):
    slots.append(0)

fileN = input("Write a script file-name: ")
if fileN == "":
    Error("Script file-name can't be nothing!")
else:
    file = None
    try:
        file = open(fileN, 'r', encoding='utf-8')
    except:
        Error("Uncorrect script file-name!")
    AnimationPrinting("Creating a int-array with 5000 slots...", 0.05)
    time.sleep(0.5)
    AnimationPrinting("Created!", 0.05)
    for line in file.readlines():
        for symbol in line:
            match symbol:
                case ">":
                    cursor_position += 1
                    if cursor_position > 5000:
                        cursor_position = 5000
                case "<":
                    cursor_position -= 1
                    if cursor_position < 1:
                        cursor_position = 1
                case "?":
                    value = input("")
                    if value != "":
                        slots[cursor_position-1] = ord(value[0])
                case ".":
                    print(special+chr(slots[cursor_position-1]), end="")
                case "+":
                    slots[cursor_position-1] += 1
                case "-":
                    slots[cursor_position-1] -= 1
                case "*":
                    slots[cursor_position-1] += 10
                case "/":
                    slots[cursor_position-1] -= 10
                case "$":
                    slots[cursor_position-1] += 100
                case "#":
                    slots[cursor_position-1] -= 100
                case "^":
                    slots[cursor_position-1] += 1000
                case "!":
                    slots[cursor_position-1] -= 1000
                case "g":
                    special = "%s" % Fore.GREEN
                case "r":
                    special = "%s" % Fore.RED
                case "y":
                    special = "%s" % Fore.YELLOW
                case "b":
                    special = "%s" % Fore.BLUE
                case ":":
                    cursor_position += 10
                    if cursor_position > 5000:
                        cursor_position = 5000
                case ";":
                    cursor_position -= 10
                    if cursor_position < 1:
                        cursor_position = 1
                case _: pass
    print("")
    AnimationPrinting("Program is finished!", 0.05)
    input("Click enter to exit from a program...")
