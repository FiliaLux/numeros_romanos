from calculatum.interface import *

def run():
    prompt()
    o = op_input("Choose an operation: ",(operators))
    print(f"{o} -> {operators[o]}")
    n1 = num_input("Enter first number: ")
    n2 = num_input("Enter second number: ")
    res = operation(n1,n2,o)
    print(f"{n1} {operators[o]} {n2} = {res} ")
    