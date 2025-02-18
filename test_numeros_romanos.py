import numeros_romanos
import calc_num_romanos
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
    assert calc_num_romanos.romano_a_int("XIX") == 19
    assert calc_num_romanos.romano_a_int("CCXXXIV") == 234
    assert calc_num_romanos.romano_a_int("XX") != 30
    assert calc_num_romanos.romano_a_int("") == 0
    assert calc_num_romanos.romano_a_int("MMM") != 4000

#Excepcion de valor de entrada incorrecto
def test_valid_roman_character():
    with pytest.raises(calc_num_romanos.RomanNumeralError) as context:
        calc_num_romanos.romano_a_int("XWY")
    assert str(context.value).endswith(" not a valid roman numeral")

#Excepción de numero de valores de entrada incorrectos
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

def valid_roman_repetitions(roman:str):
    needle = ""
    valid = False
    for key in reversed(roman):
        if key in "IXCM":
            valid = in_strike(roman,key,4)
            if valid:
                needle = key
                break
        else:
            valid = in_strike(roman,key,2)
            if valid:
                needle = key
                break
            else:
                valid = False
                needle = None
    
    return not valid, needle

def test_valid_roman_repetitons():
    assert valid_roman_repetitions("XVII") == (True,None)
    assert valid_roman_repetitions("VV") == (False,"V")
    assert valid_roman_repetitions("XXXX") == (False,"X")
    assert valid_roman_repetitions("CCLXXXVIII") == (True,None)

def test_exception_roman_repetitions():
    with pytest.raises(calc_num_romanos.RomanNumeralError) as context:
        calc_num_romanos.romano_a_int("CCLXXVIIII")
    assert str(context.value).endswith(" repeated more than admitted")
    

