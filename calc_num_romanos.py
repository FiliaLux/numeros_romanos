import numeros_romanos
num_symbols = ["+","-","*","/","**","(",")","%","="]
def romano_a_int(num:str):
    number = 0
    prev_number = 0
    for roman in reversed(num):
        if prev_number > numeros_romanos.numeros_romanos[roman]:
            number -= numeros_romanos.numeros_romanos[roman]
        else:
            number += numeros_romanos.numeros_romanos[roman]
        prev_number = numeros_romanos.numeros_romanos[roman]
    return number 

def number_input():
    number = input("Enter number: ")
    symbol = input("Enter operation: ")
    operation = ""
    while True:
        if number != "" and symbol in num_symbols:
            operation += number + " "
            operation += symbol + " "
            number = input("Enter number: ")
            symbol = input("Enter operation: ")
            if symbol == "=":
                operation += number + " "
                operation += symbol + " "
                break
        else: 
            operation = ""
            break
    print(operation)
def calculator(operation:str):
    result = 0
   