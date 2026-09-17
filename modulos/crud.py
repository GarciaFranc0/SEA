from .validaciones import validar_legajo, validar_nota


def agregar_estudiante(estudiantes, id_alumno, nombre, apellido, legajo):
    if not validar_legajo(legajo):
        print("El legajo debe contener solo dígitos.")
        return False

    for estudiante in estudiantes:
        if estudiante.get("id") == id_alumno:
            print("El ID del estudiante ya existe. No se puede agregar.")
            return False

        if estudiante.get("legajo") == legajo:
            print("El legajo del estudiante ya existe. No se puede agregar.")
            return False

    nuevo_estudiante = {
        "id": id_alumno,
        "nombre": nombre,
        "apellido": apellido,
        "legajo": legajo,
    }
    estudiantes.append(nuevo_estudiante)
    print("Estudiante registrado con éxito.")
    return True

def agregar_materia(materias, id_materia, nombre_materia):
    ids_existentes = list(filter(lambda m: m[0] == id_materia, materias))
    
    if len(ids_existentes) > 0:
        print("El ID de la materia ya existe. No se puede agregar.")
    else:
        materias.append([id_materia, nombre_materia])
        print("Materia registrada con éxito.")

def agregar_calificacion(calificaciones, id_materia, id_estudiante, nota):
    if not validar_nota(nota):
        print("La nota debe ser un número entre 0 y 10.")
        return False

    nota = float(nota)
    ids_existentes = list(filter(lambda c: c[0] == id_materia and c[1] == id_estudiante, calificaciones))
    if len(ids_existentes) > 0:
        print("La calificación ya existe. No se puede agregar.")
        return False
    else:
        calificaciones.append([id_materia, id_estudiante, nota])
        print("Calificación registrada con éxito.")
        return True

def buscar_estudiante(estudiantes, id_alumno):
    for estudiante in estudiantes:
        if estudiante.get("id") == id_alumno:
            return estudiante
    return None

def buscar_materia(materias, id_materia):
    coincidencias = list(filter(lambda m: m[0] == id_materia, materias))
    if len(coincidencias) > 0:
        return coincidencias[0]
    return None

def buscar_calificacion(calificaciones, id_materia, id_estudiante):
    coincidencias = list(filter(lambda c: c[0] == id_materia and c[1] == id_estudiante, calificaciones))
    resultado = "La calificación no existe."
    if len(coincidencias) > 0:
        resultado = coincidencias[0]
    return resultado

def eliminar_estudiante(estudiantes, id_alumno):
    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        print("El estudiante no existe.")
        return False

    estudiantes.remove(estudiante)
    print("Estudiante eliminado correctamente.")
    return True
    
def eliminar_materia(materias, id):
    for materia in materias:
        if materia[0] == id:
            materias.remove(materia)
            print("Materia eliminada correctamente.")
            return True
    print("La materia no existe.")
    return False

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

def actualizar_estudiante(estudiantes, id_alumno, nuevo_nombre, nuevo_apellido, nuevo_legajo):
    if not validar_legajo(nuevo_legajo):
        print("El legajo debe contener solo dígitos.")
        return False

    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        print("El estudiante no existe.")
        return False

    for otro_estudiante in estudiantes:
        mismo_estudiante = otro_estudiante.get("id") == id_alumno
        mismo_legajo = otro_estudiante.get("legajo") == nuevo_legajo
        if not mismo_estudiante and mismo_legajo:
            print("El nuevo legajo ya pertenece a otro estudiante.")
            return False

    estudiante.update({
        "nombre": nuevo_nombre,
        "apellido": nuevo_apellido,
        "legajo": nuevo_legajo,
    })
    print("Estudiante actualizado correctamente.")
    return True
    
def actualizar_materia(materias ,id, nueva_materia):
    for materia in materias:
        if materia[0] == id:
            materia[1] = nueva_materia
            print("Materia actualizada correctamente.")
    if id not in [materia[0] for materia in materias]:
        print("La materia no existe.")

def actualizar_calificacion(calificaciones, id_materia, id_estudiante, nueva_calificacion):
    if not validar_nota(nueva_calificacion):
        print("La nota debe ser un número entre 0 y 10.")
        return False

    nueva_calificacion = float(nueva_calificacion)
    encontrado = False
    for calificacion in calificaciones:
        if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
            calificacion[2] = nueva_calificacion
            encontrado = True          
    if encontrado:
        print("Calificación actualizada correctamente.")
        return True
    else:
        print("La calificación no existe.")
        return False

def mostrar_estudiantes(estudiantes, id_alumno):
    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        print("El estudiante no existe.")
        return

    print(
        f"ID: {estudiante.get('id')} | "
        f"Nombre: {estudiante.get('nombre')} {estudiante.get('apellido')} | "
        f"Legajo: {estudiante.get('legajo')}"
    )

def mostrar_materias(materias, id_materia):
    materia = buscar_materia(materias, id_materia)
    if materia is not None:
        print(f"ID: {materia[0]} | Nombre: {materia[1]}")
    else:
        print("La materia no existe.")

def mostrar_calificaciones(estudiantes, materias, calificaciones, id_estudiante):
    calificaciones_estudiante = [cal for cal in calificaciones if cal[1] == id_estudiante]
    if calificaciones_estudiante:
        estudiante_por_id = {estudiante.get("id"): estudiante for estudiante in estudiantes}
        materia_por_id = {materia[0]: materia for materia in materias}

        for calificacion in calificaciones_estudiante:
            estudiante = estudiante_por_id.get(calificacion[1])
            materia = materia_por_id.get(calificacion[0])

            if estudiante is None or materia is None:
                print("No se pudo mostrar una calificación porque falta el estudiante o la materia.")
                continue

            print(
                f"{estudiante.get('nombre')} {estudiante.get('apellido')} obtuvo "
                f"{calificacion[2]} en {materia[1]}"
            )
    else:
        print("No hay calificaciones registradas para este estudiante.")
