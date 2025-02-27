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
    if num > 3999:
         roman = long_number_calc(num)
    return roman

#Función que recibe numeros grandes y los devuelve en romanos 
# con asteriscos según millares
def long_number_calc(num):
    number = ""
    num_roman = []
    roman = ""
    #Añadimos los dos ceros en caso de quedar 
    # alguna cifra fuera de las tripletas para incluirla
    num = "00" + str(num) 
    #Cogemos la lista en reverso de tres en tres devolviendo 
    # el indice de posicion de cada final de tripleta
    for i in range(len(num)-1,-1,-3):
        number += num[i-2:i+1] # Sumamos a la cadena number la agrupación de tres segun la posicion del indice
    # Creamos una lista con esta cadena en grupos de tres
    for i in range(0,len(number),3): 
        num_roman.append(number[i:i+3])
    #Le damos la vuelta y devolvemos la conversión a romanos de cada
    # elemento en el orden correspondiente y con asteriscos segun indice
    for i in range(len(num_roman)-1,-1,-1): 
        if int(num_roman[i]) != 0:
            roman += int_a_romanos(int(num_roman[i]))  + ("*" * i)
        else:
            roman += ""
    return roman