result = 0
numeros_romanos = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def a_romanos(num:int) -> str:
    roman = ""
    for key, value in numeros_romanos.items():
        if value == num:
            roman = key
    return roman


assert a_romanos(1) == "I"
assert a_romanos(6) != "V"


