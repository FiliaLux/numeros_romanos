import numeros_romanos
from calc_num_romanos import romano_a_int
from calc_num_romanos import RomanNumeralError
from calc_num_romanos import valid_roman_repetitions
import pytest

#Pruebas para ejecutar con pytest del coversor de entero a romano
def test_correct_roman_conversion():
    assert numeros_romanos.a_romanos(1) == "I"
    assert numeros_romanos.a_romanos(6) != "V"
    assert numeros_romanos.int_a_romanos(456) == "CDLVI"
    assert numeros_romanos.int_a_romanos(93) != "LXXXXIII"
    assert numeros_romanos.int_a_romanos(0) == None

#Pruebas del conversor de romano a entero
def test_correct_int_conversion():
    assert romano_a_int("XIX") == 19
    assert romano_a_int("CCXXXIV") == 234
    assert romano_a_int("XX") != 30
    assert romano_a_int("") == 0
    assert romano_a_int("MMM") != 4000

#Excepcion de valor de entrada incorrecto
def test_valid_roman_character():
    with pytest.raises(RomanNumeralError) as context:
        romano_a_int("XWY")
    assert str(context.value).endswith(" not a valid roman numeral")

#Excepción de numero de valores de entrada incorrectos
def test_valid_roman_repetitons():
    assert valid_roman_repetitions("XVII") == (True,None,None)
    assert valid_roman_repetitions("VV") == (False,"V",2)
    assert valid_roman_repetitions("XXXX") == (False,"X",4)
    assert valid_roman_repetitions("CCLXXXVIII") == (True,None,None)

def test_exception_roman_repetitions():
    with pytest.raises(RomanNumeralError) as context:
        romano_a_int("CCLXXVIIII")
    assert str(context.value).endswith("be repeated 3 times")

def test_correct_subtractions():
    with pytest.raises(RomanNumeralError) as context:
        romano_a_int("XVX")
    assert str(context.value).endswith("valid substraction")

def test_repeated_substraction():
    with pytest.raises(RomanNumeralError):
        assert romano_a_int("XCXC")
    with pytest.raises(RomanNumeralError):
        assert romano_a_int("XCX")
    with pytest.raises(RomanNumeralError) as context:
        assert romano_a_int("XCXL")
    assert str(context.value).endswith("can't be admitted")

class RomanNumber:
    
    def __init__(self,num:int|str):
        
        self.value = num if int(num) else romano_a_int(num)
        self.key = numeros_romanos.int_a_romanos(num) if int(num) else num

def test_roman_number_class():
    rn = RomanNumber(8)
    assert rn.value == 8
    assert rn.key == "VIII"