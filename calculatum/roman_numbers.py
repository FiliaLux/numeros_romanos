# Diccionario de caracteres romanos
numeros_romanos = {
    "I": 1,"IV": 4,"V": 5,"IX": 9,
    "X": 10,"XL": 40,"L": 50,"XC": 90,
    "C": 100,"CD": 400,"D": 500,"CM": 900,
    "M": 1000
}

# Función de conversión de int a romano mediante diccionario
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

# Función que determina si un elemento está en racha
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

# Función que comprueba repeticiones válidas de números romanos
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

# Definición del error: RomanNumeralError
class RomanNumeralError(Exception):
    pass

# Conversión de número romano de tipo cadena a int
def romano_a_int(num:str):
    
    number = 0
    prev_number = 0
    valid, needle, limit = valid_roman_repetitions(num)
    
    if not valid:
        raise RomanNumeralError(f"{needle} {"can only be repeated 3 times" if limit == 4 else "can't be repeated"}")
    
    for roman in reversed(num):
        if roman not in numeros_romanos:
            raise RomanNumeralError(f"{roman} is not a valid roman numeral")
        if prev_number > numeros_romanos[roman]:
            if number >= prev_number + numeros_romanos[roman]:
                raise RomanNumeralError(f"Certain operations can't be admitted")
            if roman == "I" and prev_roman in "VX":
                number -= numeros_romanos[roman]
            elif roman == "X" and prev_roman in "LC":
                number -= numeros_romanos[roman]
            elif roman == "C" and prev_roman in "DM":
                number -= numeros_romanos[roman]
            else:
                raise RomanNumeralError(f"{roman}{prev_roman} is not a valid substraction")
        elif number + numeros_romanos[roman] < 4000:
            number += numeros_romanos[roman]
        prev_number = numeros_romanos[roman]
        prev_roman = roman

    return number

# Clase de números romanos
class RomanNumber():

    def __init__(self,num):
        self.value = num if isinstance(num,int) else romano_a_int(num)
        self.key = num if isinstance(num,str) else int_a_romanos(num)

    def __str__(self):
        return self.key
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, RomanNumber):
            return False
        else:
            return self.value == other.value

    def __hash__(self):
        return (self.value)

    def __lt__(self, other): #less than
        pass

    def __le__(self, other): #less equal
        pass

    def __gt__(self, other): #greater than
        pass

    def __ge__(self, other): #greater equal
        pass

    def __ne__(self, other): #not equal
        pass
    
    def __add__(self, other): #sum method // doesn't allow negative result
        sum = 0
        if isinstance(other, RomanNumber):
            if other.value < 0:
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome")
            sum = self.value + other.value
        elif isinstance(other, int):
            if other < 0: 
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome")
            sum = self.value + other
        elif isinstance(other, str):
            if romano_a_int(other) < 0:
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome.")
            sum = self.value + romano_a_int(other)
        else:
            raise TypeError(f"unsupported operation '+' between 'RomanNumber' and '{other.__class__}' type.")
        return self.__class__(sum)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other): #subtraction // doesn't allow negative result
        sub = 0
        if isinstance(other, RomanNumber): 
            if other.value > self.value:
                raise RomanNumeralError(f"Second value {other.value} can't be lower than {self.value}, can't expect negative outcome")
            sub = self.value - other.value
        elif isinstance(other, int):
            if other > self.value:
                raise RomanNumeralError(f"Second value {other} can't be lower than {self.value}, can't expect negative outcome")
            sub = self.value - other
        elif isinstance(other, str):
            if romano_a_int(other) > self.value:
                raise RomanNumeralError(f"Second value {other} can't be lower than {self.value}, can't expect negative outcome")
            sub = self.value - romano_a_int(other)
        else:
            raise TypeError(f"unsupported operation '-' between 'RomanNumber' and '{other.__class__}' type.")
        return self.__class__(sub)

    def __rsub__(self, other):
        sub = 0
        if isinstance(other, int):
            if other < self.value:
                raise RomanNumeralError(f"Second value {other} can't be lower than {self.value}, can't expect negative outcome")
            sub = other - self.value
        elif isinstance(other, str):
            if romano_a_int(other) < self.value:
                raise RomanNumeralError(f"Second value {other} can't be lower than {self.value}, can't expect negative outcome")
            sub = romano_a_int(other) - self.value
        else:
            raise TypeError(f"unsupported operation '-' between 'RomanNumber' and '{other.__class__}' type.")
        
        return self.__class__(sub)

    def __mul__(self, other): #multiplication // doesn't allow negative result
        mul = 0
        if isinstance(other, RomanNumber):
            if other.value < 0:
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome")
            mul = self.value * other.value
        elif isinstance(other, int):
            if other < 0: 
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome")
            mul = self.value * other
        elif isinstance(other, str):
            if romano_a_int(other) < 0:
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome.")
            mul = self.value * romano_a_int(other)
        else:
            raise TypeError(f"unsupported operation '*' between 'RomanNumber' and '{other.__class__}' type.")
        return self.__class__(mul)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other): #division // doesn't allow negative result
        div = 0
        if isinstance(other, RomanNumber):
            if other.value < 0:
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome")
            div = round(self.value / other.value, 0)
        elif isinstance(other, int):
            if other < 0: 
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome")
            div = round(self.value / other, 0)
        elif isinstance(other, str):
            if romano_a_int(other) < 0:
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome.")
            div = round(self.value / romano_a_int(other), 0)
        else:
            raise TypeError(f"unsupported operation '/' between 'RomanNumber' and '{other.__class__}' type.")
        return self.__class__(int(div))
    
    def __rtruediv__(self, other):
        div = 0
        if isinstance(other, int):
            if self.value < 0: 
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome")
            div = round(other / self.value, 0)
        elif isinstance(other, str):
            if self.value < 0:
                raise RomanNumeralError(f"Second value {other} can't be lower than 0, can't expect negative outcome.")
            div = round(romano_a_int(other) / self.value, 0)
        else:
            raise TypeError(f"unsupported operation '/' between 'RomanNumber' and '{other.__class__}' type.")
        return self.__class__(int(div))

    def __mod__(self, other):
        mod = 0
        if isinstance(other, RomanNumber):
            if other.value == 0:
                raise RomanNumeralError(f"Second value can't be 0, can't expect negative outcome")
            mod = self.value % other.value
        elif isinstance(other, int):
            if other == 0:
                raise RomanNumeralError(f"Second value can't be 0, can't expect negative outcome")
            mod = self.value % other
        elif isinstance(other, str):
            if romano_a_int(other) == 0:
                raise RomanNumeralError(f"Second value can't be 0, can't expect negative outcome")
            mod = self.value % romano_a_int(other)
        else:
            raise TypeError(f"unsupported operation '%' between 'RomanNumber' and '{other.__class__}' type.")
        if mod <= 0:
            raise RomanNumeralError("Can't expect 0 or negative outcome")
        return self.__class__(int(mod))
