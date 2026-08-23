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

def mostrar_calificaciones(id_estudiante):
    calificaciones_estudiante = [cal for cal in calificaciones if cal[1] == id_estudiante]
    if calificaciones_estudiante:
        for calificacion in calificaciones_estudiante:
            print(estudiantes[calificacion[1]-1][1], "obtuvo", calificacion[2], "en", materias[calificacion[0]-1][1])
    else:
        print("No hay calificaciones registradas para este estudiante.")

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
    for calificacion in calificaciones:
        if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
            calificacion_encontrada = calificacion
    if calificacion_encontrada not in calificaciones:
        calificacion_encontrada = "La calificación no existe."
    return calificacion_encontrada



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
    for calificacion in calificaciones:
        if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
            calificaciones.remove(calificacion)
            print("Calificación eliminada correctamente.")
    if [id_materia, id_estudiante] not in [[cal[0], cal[1]] for cal in calificaciones]:
        print("La calificación no existe.")


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
        for calificacion in calificaciones:
            if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
                calificacion[2] = nueva_calificacion
                print("Calificación actualizada correctamente.")
        if [id_materia, id_estudiante] not in [[cal[0], cal[1]] for cal in calificaciones]:
            print("La calificación no existe.")

def calcular_promedio(id_estudiante):
    calificaciones_estudiante = [cal[2] for cal in calificaciones if cal[1] == id_estudiante]
    if calificaciones_estudiante:
        print(f"El promedio de el/la estudiante {estudiantes[id_estudiante-1][1]} es: {sum(calificaciones_estudiante) / len(calificaciones_estudiante)}")
    else:
        print("El estudiante no tiene calificaciones registradas.")



# Matrices de entidades
estudiantes = [[1, "Franco", "Garcia", 1001], [2, "Maria", "Lopez", 1002], [3, "Juan", "Perez", 1003], [4, "Ana", "Gomez", 1004], [5, "Luis", "Martinez", 1005]]
materias = [[1, "Programacion"], [2, "Matematicas"], [3, "Fisica"], [4, "Quimica"], [5, "Historia"]]
calificaciones = [[1, 1, 10], [2, 1, 5], [3, 1, 2], [4, 1, 3], [5, 1, 9], [1, 2, 2], [2, 2, 4], [3, 2, 5], [4, 2, 7], [5, 2, 3], [1, 3, 4], [2, 3, 6], [3, 3, 2], [4, 3, 10], [5, 3, 0], [1, 4, 8], [2, 4, 9], [3, 4, 8], [4, 4, 7], [5, 4, 5], [1, 5, 10], [2, 5, 9], [3, 5, 2], [4, 5, 3], [5, 5, 0]]

# Menu principal
mostrar_calificaciones(2)
prom = calcular_promedio(2)
