from functools import reduce

def calcular_promedio(calificaciones, id_estudiante):
    calificaciones_estudiante = [cal for cal in calificaciones if cal[0][1] == id_estudiante]
    if calificaciones_estudiante:
        notas = [cal[1] for cal in calificaciones_estudiante]
        return sum(notas) / len(notas)
    return 0.0

def porcentaje_aprobados(calificaciones, id_materia):
    calificaciones_materia = list(filter(lambda c: c[0][0] == id_materia, calificaciones))
    porcentaje = 0.0
    if calificaciones_materia:
        aprobados = list(filter(lambda c: c[1] >= 4, calificaciones_materia))
        porcentaje = (len(aprobados) / len(calificaciones_materia)) * 100
    return porcentaje

def notas_extremas(calificaciones):
    nota_max = 0
    nota_min = 0
    if calificaciones:
        nota_min = calificaciones[0][1]
        nota_max = calificaciones[0][1]
        for cal in calificaciones:
            if cal[1] > nota_max:
                nota_max = cal[1]
            elif cal[1] < nota_min:
                nota_min = cal[1]
    return (nota_min, nota_max)

def porcentaje_promedio_alto(estudiantes, calificaciones):
    alumnos_calif_alta = 0
    total_estudiantes = len(estudiantes)
    if total_estudiantes > 0:
        for estudiante in estudiantes:
            id_est = estudiante.get("id")
            promedio = calcular_promedio(calificaciones, id_est)    
            if promedio >= 8.0:
                alumnos_calif_alta += 1         
        return (alumnos_calif_alta / total_estudiantes) * 100     
    return 0.0

# modulos/estadisticas.py

def estadistica_completa_estudiante(estudiantes, calificaciones, materias, id_estudiante):
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

def promedio_materia(calificaciones, id_materia):
    notas_materia = [cal[1] for cal in calificaciones if cal[0][0] == id_materia]
    return sum(notas_materia) / len(notas_materia) if notas_materia else 0.0
