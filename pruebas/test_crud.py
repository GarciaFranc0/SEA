from modulos.crud import buscar_estudiante, agregar_estudiante, eliminar_estudiante, actualizar_estudiante

def obtener_estudiantes():
    return [
        [1, "Franco", "Garcia", 1001],
        [2, "Maria", "Lopez", 1002],
        [3, "Juan", "Perez", 1003]
    ]

def obtener_calificaciones():
    return [
        [(1, 1), 10], 
        [(2, 2), 8], 
        [(1, 2), 5]
    ]

def test_buscar_estudiante():
    estudiantes = obtener_estudiantes()
    assert buscar_estudiante(estudiantes, 1) == [1, "Franco", "Garcia", 1001]
    assert buscar_estudiante(estudiantes, 3) == [3, "Juan", "Perez", 1003]
    assert buscar_estudiante(estudiantes, 4) is None

def test_agregar_estudiante():
    estudiantes = obtener_estudiantes()
    agregar_estudiante(estudiantes, 4, "Ana", "Gomez", 1004)
    assert len(estudiantes) == 4
    assert estudiantes[3] == [4, "Ana", "Gomez", 1004]

def test_eliminar_estudiante():
    estudiantes = obtener_estudiantes()
    calificaciones = obtener_calificaciones()
    eliminar_estudiante(estudiantes, calificaciones, 2)
    assert len(estudiantes) == 2
    assert buscar_estudiante(estudiantes, 2) is None
    assert len(calificaciones) == 1
    assert calificaciones[0][0] == (1, 1)

def test_actualizar_estudiante():
    estudiantes = obtener_estudiantes()
    actualizar_estudiante(estudiantes, 2, "Mariana", "Lopez", 9999) 
    assert estudiantes[1][1] == "Mariana"
    assert estudiantes[1][3] == 9999
    assert len(estudiantes) == 3