import numeros_romanos

num_symbols = ["+","-","*","/","**","(",")","%","="]

def in_strike(haystack:str,needle:str,strike:int):
    count = 0
    if len(haystack) >= strike:
        for item in haystack:
            if item == needle:
                count += 1
                if count == strike:
                    break
            else:
                count = 0
    else:
        count = 0
    
    return count >= strike

def valid_roman_repetitions(roman:str):
    needle = ""
    limit = 0
    valid = False
    for key in reversed(roman):
        if key in "IXCM":
            valid = in_strike(roman,key,4)
            if valid:
                needle = key
                limit = 4
                break
        elif key in "VLD":
            valid = in_strike(roman,key,2)
            if valid:
                needle = key
                limit = 2
                break
            else:
                valid = False
                needle = None
                limit = None
    
    return not valid, needle, limit

class RomanNumeralError(Exception):
    pass

def romano_a_int(num:str):
    
    number = 0
    prev_number = 0
    valid, needle, limit = valid_roman_repetitions(num)
    
    if not valid:
        raise RomanNumeralError(f"{needle} {"can only be repeated 3 times" if limit == 4 else "can't be repeated"}")
    
    for roman in reversed(num):
        if roman not in numeros_romanos.numeros_romanos:
            raise RomanNumeralError(f"{roman} is not a valid roman numeral")
        if prev_number > numeros_romanos.numeros_romanos[roman]:
            if number >= prev_number + numeros_romanos.numeros_romanos[roman]:
                raise RomanNumeralError(f"Certain operations can't be admitted")
            if roman == "I" and prev_roman in "VX":
                number -= numeros_romanos.numeros_romanos[roman]
            elif roman == "X" and prev_roman in "LC":
                number -= numeros_romanos.numeros_romanos[roman]
            elif roman == "C" and prev_roman in "DM":
                number -= numeros_romanos.numeros_romanos[roman]
            else:
                raise RomanNumeralError(f"{roman}{prev_roman} is not a valid substraction")
        elif number + numeros_romanos.numeros_romanos[roman] < 4000:
            number += numeros_romanos.numeros_romanos[roman]
        prev_number = numeros_romanos.numeros_romanos[roman]
        prev_roman = roman

    return number

def number_input():
    
    print("Enter operation:\n")
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
    print(f"{operation}\n")
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
            if i == 0:
                result = nums[0]
            if operator == "*":
                if operators[i-1] == "-":
                    result -= nums[i] * nums[i+1]
                elif operators[i-1] == "+":
                    result += nums[i] * nums[i+1]
                else:
                    result *= nums[i+1]
            elif operator == "/":
                if operators[i-1] == "-":
                    result -= nums[i] / nums[i+1]
                elif operators[i-1] == "+":
                    result += nums[i] / nums[i+1]
                else:
                    result /= nums[i+1]
            elif operator == "+":
                if operators[i+1] in "*/":
                    pass
                else:
                    result += nums[i+1] 
            elif operator == "-":
                if operators[i+1] in "*/":
                    pass
                else:
                    result -= nums[i+1]
            elif operator == "=":
                print(f"{int(result)} or {numeros_romanos.int_a_romanos(result)}")
