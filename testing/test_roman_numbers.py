from calculatum.roman_numbers import RomanNumber, romano_a_int, int_a_romanos, valid_roman_repetitions, RomanNumeralError
import pytest

#Pruebas para ejecutar con pytest del coversor de entero a romano
def test_correct_roman_conversion():
    assert int_a_romanos(456) == "CDLVI"
    assert int_a_romanos(93) != "LXXXXIII"
    assert int_a_romanos(0) == None

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

#Prueba de numero de valores de entrada incorrectos
def test_valid_roman_repetitons():
    assert valid_roman_repetitions("XVII") == (True,None,None)
    assert valid_roman_repetitions("VV") == (False,"V",2)
    assert valid_roman_repetitions("XXXX") == (False,"X",4)
    assert valid_roman_repetitions("CCLXXXVIII") == (True,None,None)

#Excepcion de repeticiones incorrectas
def test_exception_roman_repetitions():
    with pytest.raises(RomanNumeralError) as context:
        romano_a_int("CCLXXVIIII")
    assert str(context.value).endswith("be repeated 3 times")

#Excepcion de operaciones incorrectas dentro del número
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

#Pruebas de retorno de valores correcto de la clase RomanNumber
def test_roman_number_class():
    rn = RomanNumber(8)
    assert rn.value == 8
    assert rn.key == "VIII"

def test_roman_number_class_sum():
    a = RomanNumber("V")
    b = RomanNumber(7)

    assert a + b == RomanNumber("XII")
    assert a + 3 == RomanNumber("VIII")
    assert b + "IV" == RomanNumber("XI")

def test_roman_number_class_sub():
    a = RomanNumber("V")
    b = RomanNumber(7)

    assert b - a == RomanNumber("II")
    assert a - 3 == RomanNumber("II")
    assert b - "V" == RomanNumber("II")

def test_roman_number_class_mult():
    a = RomanNumber("V")
    b = RomanNumber(7)

    assert a * b == RomanNumber("XXXV")
    assert a * 3 == RomanNumber("XV")
    assert b * "II" == RomanNumber("XIV")

#Excepcion resta negativa
def test_class_sub_exception():
    a = RomanNumber("V")
    b = RomanNumber(7)
    
    with pytest.raises(RomanNumeralError) as context:
        
        a - b
    
    assert str(context.value).endswith("negative outcome")