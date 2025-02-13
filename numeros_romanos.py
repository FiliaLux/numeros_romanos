#Diccionario de números romanos clave y su respectivo valor
numeros_romanos = {
    "I": 1,"IV": 4,"V": 5,"IX": 9,
    "X": 10,"XL": 40,"L": 50,"XC": 90,
    "C": 100,"CD": 400,"D": 500,"CM": 900,
    "M": 1000
}

#Primera función de prueba que devuelve el valor clave correspondiente 
# al número de entrada
def a_romanos(num:int) -> str:
    roman = ""
    for key, value in numeros_romanos.items():
        if value == num:
            roman = key
    return roman

#Función final que devuelve el número romano completo correspondiente 
# al número de entrada
def int_a_romanos(num:int):
    dictionary = sorted(numeros_romanos.items(), key = lambda x: x[1], reverse = True)
    roman = ""
    if num == 0:
        roman = None
    for key, value in dictionary:
        while 4000 > num >= value:
            roman += key
            num -= value
    return roman