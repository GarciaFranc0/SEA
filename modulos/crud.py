def agregar_estudiante(estudiantes, id_alumno, nombre, apellido, legajo):
    ids_existentes = list(filter(lambda e: e[0] == id_alumno, estudiantes))
    if len(ids_existentes) > 0:
        print("El ID del estudiante ya existe. No se puede agregar")
    else:
        estudiantes.append([id_alumno, nombre, apellido, legajo])
        print("Estudiante registrado con éxito.")

def agregar_materia(materias, id_materia, nombre_materia):
    if id_materia in materias:
        print("El ID de la materia ya existe. No se puede agregar.")
    else:
        materias[id_materia] = {'nombre': nombre_materia}
        print("Materia registrada con éxito.")

def agregar_calificacion(calificaciones, id_materia, id_estudiante, nota):
    if nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10. No se puede agregar.")
        return
    clave = (id_materia, id_estudiante)

    for fila in calificaciones: 
        if fila[0] == clave:
            print("La calificación ya existe. No se puede agregar.")
            return
   
    calificaciones.append([clave, nota])
    print("Calificación registrada con éxito.")

def buscar_estudiante(estudiantes, id_alumno):
    coincidencias = list(filter(lambda e: e[0] == id_alumno, estudiantes))
    resultado = "El estudiante no existe"
    if len(coincidencias) > 0:
        resultado = coincidencias[0]
    return resultado

def buscar_materia(materias, id_materia):
    materia = materias.get(id_materia)
    if materia:
        resultado = materia
    else:
        resultado = "La materia no existe"
    return resultado

def buscar_calificacion(calificaciones, id_materia, id_estudiante):
    clave = (id_materia, id_estudiante)
    for fila in calificaciones:
        if fila[0] == clave:
            return fila
    return "La calificación no existe."

def eliminar_estudiante(estudiantes, id_alumno):
    encontrado = False
    for estudiante in estudiantes:
        if estudiante[0] == id_alumno:
            estudiantes.remove(estudiante)
            encontrado = True     
    if encontrado:
        print("Estudiante eliminado correctamente.")
    else:
        print("El estudiante no existe.")
    
def eliminar_materia(materias, id_materia):
    if id_materia in materias:
        del materias[id_materia]
        print("Materia eliminada correctamente.")
    else:
        print("La materia no existe.")

def eliminar_calificacion(calificaciones, id_materia, id_estudiante):
    clave = (id_materia, id_estudiante)
    for fila in calificaciones:
        if fila[0] == clave:
            calificaciones.remove(fila)
            print("Calificación eliminada correctamente.")
            return
    print("La calificación no existe.")

def actualizar_estudiante(estudiantes, id, nuevo_nombre, nuevo_apellido, nuevo_legajo):
    for estudiante in estudiantes:
        if estudiante[0] == id:
            estudiante[1] = nuevo_nombre
            estudiante[2] = nuevo_apellido
            estudiante[3] = nuevo_legajo
            print("Estudiante actualizado correctamente.")
    if id not in [estudiante[0] for estudiante in estudiantes]:
        print("El estudiante no existe.")
    
def actualizar_materia(materias ,id_materia, nueva_materia):
    if id_materia in materias:
        materias[id_materia]["nombre"] = nueva_materia
        print("Materia actualizada correctamente.")
    else:
        print("La materia no existe.")

def actualizar_calificacion(calificaciones, id_materia, id_estudiante, nueva_calificacion):
    clave = (id_materia, id_estudiante)
    for fila in calificaciones:
        if fila[0] == clave:
            fila[1] = nueva_calificacion
            print("Calificación actualizada correctamente.")
            return
    print("La calificación no existe.")

def mostrar_estudiantes(estudiantes, id_alumno):
    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante != "El estudiante no existe.":
        print(f"ID: {estudiante[0]} | Nombre: {estudiante[1]} {estudiante[2]} | Legajo: {estudiante[3]}")
    else:
        print(estudiante)

def mostrar_materias(materias, id_materia):
    materia = buscar_materia(materias, id_materia)
    if materia != "La materia no existe.":
        print(f"ID: {id_materia} | Nombre: {materia['nombre']}")
    else:
        print(materia)

def mostrar_calificaciones(estudiantes, materias, calificaciones, id_estudiante):
    calificaciones_estudiante = [
        calificacion for calificacion in calificaciones
        if calificacion[0][1] == id_estudiante
    ]

    if calificaciones_estudiante:
        estudiante = next(
            estudiante for estudiante in estudiantes
            if estudiante[0] == id_estudiante
        )

        for calificacion in calificaciones_estudiante:
            id_materia = calificacion[0][0]
            nota = calificacion[1]
            materia = materias[id_materia]

            print(f"{estudiante[1]} obtuvo {nota} en {materia['nombre']}")
    else:
        print("No hay calificaciones registradas para este estudiante.")