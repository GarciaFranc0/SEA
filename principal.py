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

def eliminar_estudiante(id):
    for estudiante in estudiantes:
        if estudiante[0] == id:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente.")
    if id not in estudiantes:
        print("El estudiante no existe.")
    
    

def eliminar_materia(id):
    for materia in materias:
        if materia[0] == id:
            materias.remove(materia)
            print("Materia eliminada correctamente.")
    if id not in materias:
        print("La materia no existe.")

def eliminar_calificacion(id_materia, id_estudiante):
    if calificaciones:
        for calificacion in calificaciones:
            if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
                calificaciones.remove(calificacion)
                print("Calificación eliminada correctamente.")
        if [id_materia, id_estudiante] not in [[cal[0], cal[1]] for cal in calificaciones]:
            print("La calificación no existe.")
    else:
        print("No hay calificaciones registradas.")

def actualizar_estudiante(id, nuevo_nombre, nuevo_apellido, nuevo_legajo):
    for estudiante in estudiantes:
        if estudiante[0] == id:
            estudiante[1] = nuevo_nombre
            estudiante[2] = nuevo_apellido
            estudiante[3] = nuevo_legajo
            print("Estudiante actualizado correctamente.")
    if id not in [estudiante[0] for estudiante in estudiantes]:
        print("El estudiante no existe.")
    

def actualizar_materia(id, nueva_materia):
    for materia in materias:
        if materia[0] == id:
            materia[1] = nueva_materia
            print("Materia actualizada correctamente.")
    if id not in [materia[0] for materia in materias]:
        print("La materia no existe.")


def actualizar_calificacion(id_materia, id_estudiante, nueva_calificacion):
    if calificaciones:
        for calificacion in calificaciones:
            if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
                calificacion[2] = nueva_calificacion
                print("Calificación actualizada correctamente.")
        if [id_materia, id_estudiante] not in [[cal[0], cal[1]] for cal in calificaciones]:
            print("La calificación no existe.")
    else:   
        print("No hay calificaciones registradas.")


# Matrices de entidades
estudiantes = [[1, "Franco", "Garcia", 1001], [2, "Maria", "Lopez", 1002], [3, "Juan", "Perez", 1003], [4, "Ana", "Gomez", 1004], [5, "Luis", "Martinez", 1005]]
materias = [[1, "Programacion"], [2, "Matematicas"], [3, "Fisica"], [4, "Quimica"], [5, "Historia"]]
calificaciones = []

# Menu principal

actualizar_estudiante(6, "Carlos", "Rodriguez", 1006)
actualizar_materia(5, "Biologia")
actualizar_calificacion(1, 2, 9.5)