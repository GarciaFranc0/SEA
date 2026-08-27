def agregar_estudiante(estudiantes, id_alumno, nombre, apellido, legajo):
    ids_existentes = list(filter(lambda e: e[0] == id_alumno, estudiantes))
    if len(ids_existentes) > 0:
        print("El ID del estudiante ya existe. No se puede agregar")
    else:
        estudiantes.append([id_alumno, nombre, apellido, legajo])
        print("Estudiante registrado con éxito.")

def agregar_materia(materias, id_materia, nombre_materia):
    ids_existentes = list(filter(lambda m: m[0] == id_materia, materias))
    
    if len(ids_existentes) > 0:
        print("El ID de la materia ya existe. No se puede agregar.")
    else:
        materias.append([id_materia, nombre_materia])
        print("Materia registrada con éxito.")

def agregar_calificacion(calificaciones, id_materia, id_estudiante, nota):
    ids_existentes = list(filter(lambda c: c[0] == id_materia and c[1] == id_estudiante, calificaciones))
    if len(ids_existentes) > 0:
        print("La calificación ya existe. No se puede agregar.")
    else:
        calificaciones.append([id_materia, id_estudiante, nota])
        print("Calificación registrada con éxito.")

def buscar_estudiante(estudiantes, id_alumno):
    coincidencias = list(filter(lambda e: e[0] == id_alumno, estudiantes))
    resultado = "El estudiante no existe"
    if len(coincidencias) > 0:
        resultado = coincidencias[0]
    return resultado

def buscar_materia(materias, id_materia):
    coincidencias = list(filter(lambda m: m[0] == id_materia, materias))
    resultado = "La materia no existe"
    if len(coincidencias) > 0:
        resultado = coincidencias[0]
    return resultado

def buscar_calificacion(calificaciones, id_materia, id_estudiante):
    coincidencias = list(filter(lambda c: c[0] == id_materia and c[1] == id_estudiante, calificaciones))
    resultado = "La calificación no existe."
    if len(coincidencias) > 0:
        resultado = coincidencias[0]
    return resultado

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
    
def eliminar_materia(id):
    for materia in materias:
        if materia[0] == id:
            materias.remove(materia)
            print("Materia eliminada correctamente.")
    if id not in materias:
        print("La materia no existe.")

def eliminar_calificacion(calificaciones, id_materia, id_estudiante):
    encontrado = False
    for calificacion in calificaciones:
        if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
            calificaciones.remove(calificacion)
            encontrado = True       
    if encontrado:
        print("Calificación eliminada correctamente.")
    else:
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

def actualizar_calificacion(calificaciones, id_materia, id_estudiante, nueva_calificacion):
    encontrado = False
    for calificacion in calificaciones:
        if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
            calificacion[2] = nueva_calificacion
            encontrado = True          
    if encontrado:
        print("Calificación actualizada correctamente.")
    else:
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
        print(f"ID: {materia[0]} | Nombre: {materia[1]}")
    else:
        print(materia)

def mostrar_calificaciones(id_estudiante):
    calificaciones_estudiante = [cal for cal in calificaciones if cal[1] == id_estudiante]
    if calificaciones_estudiante:
        for calificacion in calificaciones_estudiante:
            print(estudiantes[calificacion[1]-1][1], "obtuvo", calificacion[2], "en", materias[calificacion[0]-1][1])
    else:
        print("No hay calificaciones registradas para este estudiante.")
