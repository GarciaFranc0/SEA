from functools import reduce

def calcular_promedio(calificaciones, id_estudiante):
    calificaciones_estudiante = list(filter(lambda calificacion: calificacion[1] == id_estudiante, calificaciones))
    notas = list(map(lambda calificacion: calificacion[2], calificaciones_estudiante))
    promedio = 0.0
    if notas:
        suma_total = reduce(lambda x, y: x + y, notas)
        promedio = suma_total / len(notas)
    return promedio


def porcentaje_aprobados(calificaciones, id_materia):
    calificaciones_materia = list(filter(lambda calificacion: calificacion[0] == id_materia, calificaciones))
    porcentaje = 0.0
    if calificaciones_materia:
        aprobados = list(filter(lambda calificacion: calificacion[2] >= 4, calificaciones_materia))
        porcentaje = (len(aprobados) / len(calificaciones_materia)) * 100
    return porcentaje