from numeros_romanos import int_a_romanos
from calc_num_romanos import romano_a_int

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

    def __add__(self, other):

        if isinstance(other, RomanNumber):
            
            return int_a_romanos(self.value + other.value)

        elif isinstance(other, int):
            
            return int_a_romanos(self.value + other)

        elif isinstance(other, str):

            return int_a_romanos(self.value + romano_a_int(other))
        
        else:
            
            raise TypeError(f"unsupported operation '+' between 'RomanNumber' and '{other.__class__}' type.")

    def __substract__(self, other):

        if isinstance(other, RomanNumber):

            return int_a_romanos(self.value - other.value)

        elif isinstance(other, int):
            
            return int_a_romanos(self.value - other)

        elif isinstance(other, str):

            return int_a_romanos(self.value - romano_a_int(other))
        
        else:
            
            raise TypeError(f"unsupported operation '-' between 'RomanNumber' and '{other.__class__}' type.")