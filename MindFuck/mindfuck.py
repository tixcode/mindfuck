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
cursor_position = 0
for i in range(0, 5000):
    slots.append(0)

fileN = input("Write a script file-name: ")
if fileN == "":
    Error("Script file-name can't be nothing!")
else:
    try:
        with open(fileN, 'r', encoding='utf-8') as file:
          code = file.read()
    except:
        Error("Uncorrect script file-name!")
    AnimationPrinting("Creating a int-array with 5000 slots...", 0.05)
    time.sleep(0.5)
    AnimationPrinting("Created!", 0.05)
    index = 0
    while index < len(code):
        symbol = code[index]
        match symbol:
            case ">":
                cursor_position += 1
                cursor_position = min(cursor_position, 5000 - 1)
            case "<":
                cursor_position -= 1
                cursor_position = max(cursor_position, 0)
            case "?":
                value = input("")
                if value != "":
                    slots[cursor_position] = ord(value[0])
            case ".":
                print(special+chr(slots[cursor_position]), end="")
            case "+":
                slots[cursor_position] += 1
            case "-":
                slots[cursor_position] -= 1
            case "*":
                slots[cursor_position] += 10
            case "/":
                slots[cursor_position] -= 10
            case "$":
                slots[cursor_position] += 100
            case "#":
                slots[cursor_position] -= 100
            case "^":
                slots[cursor_position] += 1000
            case "!":
                slots[cursor_position] -= 1000
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
            case "[":
                if slots[cursor_position] == 0:
                  counter = 1
                  while counter:
                    index += 1
                    char = code[index]
                    match char:
                      case "[": counter += 1
                      case "]": counter -= 1
            case "]":
                if slots[cursor_position] != 0:
                  counter = 1
                  while counter:
                    index -= 1
                    char = code[index]
                    match char:
                      case "[": counter -= 1
                      case "]": counter += 1
            case _: pass
        index += 1
    print("")
    AnimationPrinting("Program is finished!", 0.05)
    input("Click enter to exit from a program...")
