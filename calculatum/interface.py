from calculatum.roman_numbers import *

operators = {"1": "+", "2": "-", "3": "x", "4": ":", "5": "%"}

def prompt():
    print("CALCULATUM")
    print("==========")
    print("Operations: ")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Mod")


def is_valid(num:int|str):
    try:
        int(num)
        return True
    except ValueError:
        return False

def num_input(msg):
    while True:
        num = input(f"{msg}: ")
        try:
            number = RomanNumber(int(num) if num.isdigit() else num)
            break
        except RomanNumeralError:
            print("Please enter a valid roman numeral or integer:")
    return number

def op_input(msg: str, options: tuple):
    options = tuple(map(str,options))
    while True:
        op = input(f"{msg}: ")
        if op in options:
            break
        print(f"Enter operation: {options}")
    return op

def operation(n1,n2,op):
    res = ""
    if op == "1":
        res = n1 + n2
    elif op == "2":
        res = n1 - n2
    elif op == "3":
        res = n1 * n2
    elif op == "4":
        res = n1 / n2
    elif op == "5":
        res = n1 % n2
    return res
   