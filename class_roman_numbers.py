from numeros_romanos import int_a_romanos
from calc_num_romanos import romano_a_int
from calc_num_romanos import RomanNumeralError

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
