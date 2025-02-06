result = 0
numeros_romanos = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


def a_romanos(num:int) -> str:
    roman = ""
    for key, value in numeros_romanos.items():
        if value == num:
            roman = key
    return roman

def int_a_romanos(num:int):
    dictionary = sorted(numeros_romanos.items(), key = lambda x: x[1], reverse = True)
    roman = ""
    for key, value in dictionary:
        while num >= value:
            roman += key
            num -= value
    return roman


assert a_romanos(1) == "I"
assert a_romanos(6) != "V"
assert int_a_romanos(456) == "CDLVI"
assert int_a_romanos(93) != "LXXXXIII"
