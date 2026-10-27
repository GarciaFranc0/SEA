from functools import reduce

def _promedio(calificaciones, posicion, identificador):
    # posicion 0 filtra por materia y posicion 1 por estudiante dentro de la clave (materia, estudiante)
    notas = list(map(lambda c: c[1], filter(lambda c: c[0][posicion] == identificador, calificaciones)))
    if notas:
        suma = reduce(lambda acumulado, nota: acumulado + nota, notas, 0)
        return suma / len(notas)
    return 0.0

def calcular_promedio(calificaciones, id_estudiante):
    return _promedio(calificaciones, 1, id_estudiante)

def promedio_materia(calificaciones, id_materia):
    return _promedio(calificaciones, 0, id_materia)

def porcentaje_aprobados(calificaciones, id_materia):
    calificaciones_materia = list(filter(lambda c: c[0][0] == id_materia, calificaciones))
    porcentaje = 0.0
    if calificaciones_materia:
        aprobados = list(filter(lambda c: c[1] >= 4, calificaciones_materia))
        porcentaje = (len(aprobados) / len(calificaciones_materia)) * 100
    return porcentaje

def notas_extremas(calificaciones):
    
    if len(calificaciones) == 0:
        return (0, 0)
    elif len(calificaciones) == 1:
        nota = calificaciones[0][1]
        return (nota, nota)
    else:
        nota_min, nota_max = notas_extremas(calificaciones[1:])
        nota = calificaciones[0][1]

        if nota < nota_min:
            nota_min = nota

        if nota > nota_max:
            nota_max = nota

        return (nota_min, nota_max)
    
def porcentaje_promedio_alto(estudiantes, calificaciones):
    alumnos_calif_alta = 0
    total_estudiantes = len(estudiantes)
    if total_estudiantes > 0:
        for estudiante in estudiantes:
            id_est = estudiante[0]
            promedio = calcular_promedio(calificaciones, id_est)
            if promedio >= 8.0:
                alumnos_calif_alta += 1
        return (alumnos_calif_alta / total_estudiantes) * 100
    return 0.0

def estadistica_completa_estudiante(calificaciones, id_estudiante):
    notas_estudiante = [cal[1] for cal in calificaciones if cal[0][1] == id_estudiante]
    total_materias = len(notas_estudiante)
    promedio = 0.0
    max_nota = 0.0
    min_nota = 0.0
    if notas_estudiante:
        promedio = sum(notas_estudiante) / total_materias
        max_nota = max(notas_estudiante)
        min_nota = min(notas_estudiante)
    return {
        "total": total_materias,
        "promedio": promedio,
        "maxima": max_nota,
        "minima": min_nota
    }

def estudiantes_comunes_materias(calificaciones, id_materia1, id_materia2):
    estudiantes_materia1 = set(map(lambda cal: cal[0][1], filter(lambda cal: cal[0][0] == id_materia1, calificaciones)))
    estudiantes_materia2 = set(map(lambda cal: cal[0][1], filter(lambda cal: cal[0][0] == id_materia2, calificaciones)))
    comunes = estudiantes_materia1 & estudiantes_materia2
    return comunes

def estudiantes_sin_calificacion(estudiantes, calificaciones):
    id_estudiantes = set(map(lambda est: est[0], estudiantes))
    estudiantes_con_notas = set(map(lambda cal: cal[0][1], calificaciones))
    sin_calificacion = id_estudiantes - estudiantes_con_notas
    return sin_calificacion
