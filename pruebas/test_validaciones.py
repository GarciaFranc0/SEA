from modulos.validaciones import validar_nota, validar_legajo, valores_duplicados

def test_validar_nota():

    assert validar_nota(5) == True
    assert validar_nota(7.5) == True

    assert validar_nota(10) == True
    assert validar_nota(0) == True

    assert validar_nota(-1) == False
    assert validar_nota(-0.1) == False
    assert validar_nota(10.1) == False
    assert validar_nota(11) == False

def test_validar_legajo():
    assert validar_legajo("1001") == True
    assert validar_legajo("12345") == True

    assert validar_legajo("abc") == False
    assert validar_legajo("12a34") == False
    assert validar_legajo("12 34") == False
    assert validar_legajo("-1001") == False
    assert validar_legajo("") == False

def test_valores_duplicados():
    estudiantes = [
        [1, "Franco", "Garcia", 1001],
        [2, "Maria", "Lopez", 1002],
        [3, "Juan", "Perez", 1001]
    ]
    resultado = valores_duplicados(estudiantes, 3)
    assert 1001 in resultado

    estudiantes_sin_duplicado = [
        [1, "Franco", "Garcia", 1001],
        [2, "Maria", "Lopez", 1002],
    ]
    assert not valores_duplicados(estudiantes_sin_duplicado, 3)