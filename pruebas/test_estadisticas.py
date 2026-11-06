from modulos.estadisticas import calcular_promedio, porcentaje_aprobados, notas_extremas, contar_aprobados_desaprobados, contar_registros, ultimos_registrados

def obtener_calificaciones():
    return [
        [(1, 1), 10], [(2, 1), 6], [(3, 1), 2],
        [(1, 2), 2], [(2, 2), 4], [(3, 2), 6],
        [(1, 3), 8]
    ]

def test_calcular_promedio():
    calificaciones = obtener_calificaciones()
    assert calcular_promedio(calificaciones, 1) == 6.0
    assert calcular_promedio(calificaciones, 3) == 8.0
    assert calcular_promedio(calificaciones, 4) == 0.0

def test_porcentaje_aprobados():
    calificaciones = obtener_calificaciones()
    assert porcentaje_aprobados(calificaciones, 2) == 100.0
    assert porcentaje_aprobados(calificaciones, 3) == 50.0
    assert porcentaje_aprobados(calificaciones, 4) == 0.0

def test_notas_extremas():
    calificaciones = obtener_calificaciones()
    assert notas_extremas(calificaciones) == (2, 10)
    assert notas_extremas([]) == (0, 0)
    assert notas_extremas([[(1, 1), 5]]) == (5, 5)

def test_contar_aprobados_desaprobados():
    calificaciones = obtener_calificaciones()
    assert contar_aprobados_desaprobados(calificaciones) == (5, 2)
    assert contar_aprobados_desaprobados(calificaciones, 3) == (1, 1)
    assert contar_aprobados_desaprobados(calificaciones, 9) == (0, 0)

def test_contar_registros():
    resultado = contar_registros([[1, "A", "B", 1]], [[1, "M"], [2, "N"]], obtener_calificaciones())
    assert resultado == {"estudiantes": 1, "materias": 2, "calificaciones": 7}

def test_ultimos_registrados():
    registros = [1, 2, 3, 4, 5, 6, 7, 8]
    assert ultimos_registrados(registros) == [4, 5, 6, 7, 8]
    assert ultimos_registrados(registros, 2) == [7, 8]
    assert ultimos_registrados([1, 2], 5) == [1, 2]
    assert ultimos_registrados(registros, 0) == []
