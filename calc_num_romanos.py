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
                    result += nums[i] - nums[i+1]
            elif operator == "=":
                print(int(result))
                print(numeros_romanos.int_a_romanos(result))

    