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

def notas_extremas(calificaciones):
    nota_max = 0
    nota_min = 0
    if calificaciones:
        nota_min = calificaciones[0][2]
        nota_max = calificaciones[0][2]
        for calificacion in calificaciones:
            if calificacion[2] > nota_max:
                nota_max = calificacion[2]
            elif calificacion[2] < nota_min:
                nota_min = calificacion[2]
    calificaciones_extremas = [nota_min, nota_max]
    return calificaciones_extremas

def porcentaje_promedio_alto(estudiantes, calificaciones):
    alumnos_calif_alta = 0
    for est in estudiantes:
        promedio = calcular_promedio(calificaciones, est[0])
        if promedio >= 8.0:
            alumnos_calif_alta += 1
    porcentaje = (alumnos_calif_alta / len(estudiantes)) * 100
    return porcentaje

def estadistica_completa(estudiantes, calificaciones, materias, id_estudiante):
    calif_est = []
    for calificacion in calificaciones:
        if calificacion[1] == id_estudiante:
            calif_est.append()
    total_materias = len(calif_est)
    promedio = calcular_promedio(calificaciones, id_estudiante)
    max_nota = max(calif_est)
    min_nota = min(calif_est)
    return (f"cursa: {total_materias} materias, tiene un promedio de {promedio}, su nota mas alta es: {max_nota} y su mas baja es: {min_nota}")

def promedio_materia(calificaciones, id_materia):
    notas_materia = [cal[2] for cal in calificaciones if cal[0] == id_materia]
    promedio = 0.0
    if notas_materia:
        promedio = sum(notas_materia) / len(notas_materia)
    return promedio