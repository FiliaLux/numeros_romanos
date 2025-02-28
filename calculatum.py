from calculatum.roman_numbers import numeros_romanos, romano_a_int, int_a_romanos

num_romanos = numeros_romanos.items()
operators = {"1": "+", "2": "-", "3": "x", "4": "%"}

class InputError(Exception):
    pass

def is_valid(num:int|str):
    try:
        int(num)
        return True
    except ValueError:
        return False

def calculatum_input():
    prompt = print("CALCULATUM\n==========\nChoose an operation:\n1.Sum\n2.Substraction\n3.Multiplication\n4.Division\n")
    operation = input("Enter operation: ")
    number_1 = input("Enter first number: ")
    number_2 = input("Enter second number: ")
    result = 0
    
    if operation not in operators:
        print(f"This is not a valid operator.\nPlease try again.\n{prompt}{operation}{number_1}{number_2}")
    elif not is_valid(number_1) and not is_valid(romano_a_int(number_1)):
        print(f"This is not a valid first number, try again:\n{number_1}{number_2}")
    elif not is_valid(number_2) and not is_valid(romano_a_int(number_2)):
        print(f"This is not a valid second number, try again:\n{number_2}")
    
    inumber_1 = int(number_1) if is_valid(number_1) else romano_a_int(number_1)
    inumber_2 = int(number_2) if is_valid(number_2) else romano_a_int(number_2)
    
    for num, symbol in operators.items():
        if operation == num:
            print(f"{number_1} {symbol} {number_2} = ")
        if operation == "1":
            result = inumber_1 + inumber_2
        elif operation == "2":
            result = inumber_1 - inumber_2
        elif operation == "3":
            result = inumber_1 * inumber_2
        elif operation == "4":
            result = inumber_1 / inumber_2
    
    print(f"Total: {result} or {int_a_romanos(result)}")