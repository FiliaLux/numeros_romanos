from calculatum.roman_numbers import numeros_romanos,romano_a_int,int_a_romanos

num_symbols = ["+","-","*","/","%","="]

def calculator(operation:str):
        
        num = ""
        nums = []
        operators = ""
        result = 0
        
        for element in operation:
            if element in numeros_romanos:
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
                