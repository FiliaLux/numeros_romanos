import numeros_romanos

def test_correct_conversion():
    assert numeros_romanos.a_romanos(1) == "I"
    assert numeros_romanos.a_romanos(6) != "V"
    assert numeros_romanos.int_a_romanos(456) == "CDLVI"
    assert numeros_romanos.int_a_romanos(93) != "LXXXXIII"
    assert numeros_romanos.int_a_romanos(0) == None