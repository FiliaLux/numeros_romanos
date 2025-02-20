import numeros_romanos
import test_numeros_romanos

num_symbols = ["+","-","*","/","**","(",")","%","="]

class RomanNumeralError(Exception):
    pass

def romano_a_int(num:str):
    
    number = 0
    prev_number = 0
    valid, needle, limit = test_numeros_romanos.valid_roman_repetitions(num)
    substracted = False
    
    if not valid:
        raise RomanNumeralError(f"{needle} {"can only be repeated 3 times" if limit == 4 else "can't be repeated"}")
    
    for roman in reversed(num):
        if roman not in numeros_romanos.numeros_romanos:
            raise RomanNumeralError(f"{roman} is not a valid roman numeral")
        if prev_number > numeros_romanos.numeros_romanos[roman]:
            if substracted == True and number > prev_number + numeros_romanos.numeros_romanos[roman]:
                raise RomanNumeralError(f"Certain substractions can't be repeated")
            if roman == "I" and prev_roman in "VX":
                number -= numeros_romanos.numeros_romanos[roman]
                substracted = True
            elif roman == "X" and prev_roman in "LC":
                number -= numeros_romanos.numeros_romanos[roman]
                substracted = True
            elif roman == "C" and prev_roman in "DM":
                number -= numeros_romanos.numeros_romanos[roman]
                substracted = True
            else:
                raise RomanNumeralError(f"{roman}{prev_roman} is not a valid substraction")
        elif number + numeros_romanos.numeros_romanos[roman] < 4000:
            number += numeros_romanos.numeros_romanos[roman]
            substracted += False
        prev_number = numeros_romanos.numeros_romanos[roman]
        prev_roman = roman

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
    return operation

def calculator(operation:str):
        
        num = ""
        nums = []
        operators = ""
        result = 0
        
        for element in operation:
            if element in numeros_romanos.numeros_romanos:
                num += element
            elif element in num_symbols:
                operators += element
                nums.append(romano_a_int(num))
                num = ""
        
        for i,operator in enumerate(operators):
            if operator == "*":
                if i == 1:
                    result = nums[0]
                if operators[i-1] == "-":
                    result -= nums[i] * nums[i+1]
                else:
                    result += nums[i] * nums[i+1]
            elif operator == "/":
                if i == 1:
                    result = nums[0]
                if operators[i-1] == "-":
                    result -= nums[i] / nums[i+1]
                else:
                    result += nums[i] / nums[i+1]
            elif operator == "+":
                if operators[i+1] in "*/":
                    pass
                else:
                    result += nums[i] + nums[i+1] 
            elif operator == "-":
                if operators[i+1] in "*/":
                    pass
                else:
                    result -= nums[i] - nums[i+1]
            elif operator == "=":
                print(int(result))
                print(numeros_romanos.int_a_romanos(result))