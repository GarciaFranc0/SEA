# Funciones
def agregar_estudiante(id, nombre, apellido, legajo):
    if id in [estudiante[0] for estudiante in estudiantes]:
        print("El ID del estudiante ya existe. No se puede agregar.")
    else:
        estudiantes.append([id, nombre, apellido, legajo])

def agregar_materia(id, materia):
    if id in [materia[0] for materia in materias]:
        print("El ID de la materia ya existe. No se puede agregar.")
    else:
        materias.append([id, materia])

def agregar_calificacion(id_materia, id_estudiante, calificacion):
    if [id_materia, id_estudiante] in [[cal[0], cal[1]] for cal in calificaciones]:
        print("La calificación ya existe. No se puede agregar.")
    else:
        calificaciones.append([id_materia, id_estudiante, calificacion])

def mostrar_estudiantes(id):
    if id in [estudiante[0] for estudiante in estudiantes]:
        print(estudiantes[id-1])
    else:
        print("El estudiante no existe.")

def mostrar_materias(id):
    if id in [materia[0] for materia in materias]:
        print(materias[id-1])
    else:
        print("La materia no existe.")

def mostrar_calificaciones():
    if calificaciones:
        for calificacion in calificaciones:
            print(calificacion)
    else:
        print("No hay calificaciones registradas.")

def buscar_estudiante(id):
    estudiante_encontrado = None
    for estudiante in estudiantes:
        if estudiante[0] == id:   
            estudiante_encontrado = estudiante
    if estudiante_encontrado not in estudiantes:
        estudiante_encontrado = "El estudiante no existe."
    return estudiante_encontrado

def buscar_materia(id):
    materia_encontrada = None
    for materia in materias:
        if materia[0] == id:
            materia_encontrada = materia

    if materia_encontrada not in materias:
        materia_encontrada = "La materia no existe."
    return materia_encontrada


def buscar_calificacion(id_materia, id_estudiante):
    calificacion_encontrada = None
    if calificaciones:
        for calificacion in calificaciones:
            if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
                calificacion_encontrada = calificacion
        if calificacion_encontrada not in calificaciones:
            calificacion_encontrada = "La calificación no existe."
        return calificacion_encontrada
    else:
        return "No hay calificaciones registradas."

def eliminar_estudiante():
    ...

def eliminar_materia():
    ...

def eliminar_calificacion():
    ...

def actualizar_estudiante():
    ...

def actualizar_materia():
    ...

def actualizar_calificacion():
    ...



# Matrices de entidades
estudiantes = [[1, "Franco", "Garcia", 1001], [2, "Maria", "Lopez", 1002], [3, "Juan", "Perez", 1003], [4, "Ana", "Gomez", 1004], [5, "Luis", "Martinez", 1005]]
materias = [[1, "Programacion"], [2, "Matematicas"], [3, "Fisica"], [4, "Quimica"], [5, "Historia"]]
calificaciones = []

# Menu principal

estudianteq = buscar_estudiante(1)
print(estudianteq)
materiaq = buscar_materia(1)
print(materiaq)
calificacionq = buscar_calificacion(0, 0)
print(calificacionq)