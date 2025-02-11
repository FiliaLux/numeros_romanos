import numeros_romanos
num_symbols = ["+","-","*","/","**","(",")","%","="]
def romano_a_int(num:str):
    num_reverse = sorted(numeros_romanos.numeros_romanos.items(), key = lambda x:x[1], reverse = True)
    number = 0
    accum = ""
    for key, value in num_reverse:
        for roman in num:
            if key == roman:
                accum += key
                number += value
                if accum in numeros_romanos.numeros_romanos.items():
                    number += numeros_romanos.numeros_romanos[accum]
                    print(accum)
                    accum = ""
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
    num = ""
    for element in operation:
        if element in "1234567890":
            num += element
        else:
            result += int(num)
            num = ""
            result += element
    print(result)