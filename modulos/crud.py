from .interfaz import subtitulo, exito, error, separador, alerta
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
    for estudiante in estudiantes:
        if estudiante.get("id") == id_alumno:
            return estudiante
    return None

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
    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        error("El estudiante no existe.")
        return False

    estudiantes.remove(estudiante)
    exito("Estudiante eliminado correctamente.")
    return True
    
def eliminar_materia(materias, id_materia):
    if id_materia in materias:
        del materias[id_materia]
        exito("Materia eliminada correctamente.")
    else:
        error("La materia no existe.")

def eliminar_calificacion(calificaciones, id_materia, id_estudiante):
    clave = (id_materia, id_estudiante)
    for fila in calificaciones:
        if fila[0] == clave:
            calificaciones.remove(fila)
            exito("Calificación eliminada correctamente.")
            return
    error("La calificación no existe.")

def actualizar_estudiante(estudiantes, id_alumno, nuevo_nombre, nuevo_apellido, nuevo_legajo):
    if not validar_legajo(nuevo_legajo):
        print("El legajo debe contener solo dígitos.")
        return False

    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        error("El estudiante no existe.")
        return False
        
    estudiante["nombre"] = nuevo_nombre
    estudiante["apellido"] = nuevo_apellido
    estudiante["legajo"] = int(nuevo_legajo)
    exito("Estudiante actualizado correctamente.")
    return True
    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        print("El estudiante no existe.")

def actualizar_materia(materias ,id_materia, nueva_materia):
    if id_materia in materias:
        materias[id_materia]["nombre"] = nueva_materia
        print("Materia actualizada correctamente.")
    else:
        error("La materia no existe.")

def actualizar_calificacion(calificaciones, id_materia, id_estudiante, nueva_calificacion):
    clave = (id_materia, id_estudiante)
    for fila in calificaciones:
        if fila[0] == clave:
            fila[1] = nueva_calificacion
            print("Calificación actualizada correctamente.")
            return
    error("La calificación no existe.")

def mostrar_estudiantes(estudiantes, id_alumno):
    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        error("El estudiante solicitado no existe.")
        return

    subtitulo("Información del Estudiante")
    print(f"  {'ID':<6} | {'NOMBRE Y APELLIDO':<25} | {'LEGAJO':<10}")
    separador()
    nombre_completo = f"{estudiante.get('nombre')} {estudiante.get('apellido')}"
    print(f"  {estudiante.get('id'):<6} | {nombre_completo:<25} | {estudiante.get('legajo'):<10}")
    separador()

def mostrar_materias(materias, id_materia):
    materia = buscar_materia(materias, id_materia)
    if materia != "La materia no existe.":
        print(f"ID: {id_materia} | Nombre: {materia['nombre']}")
    else:
        error("La materia no existe.")

def mostrar_calificaciones(estudiantes, materias, calificaciones, id_estudiante):
    estudiante = buscar_estudiante(estudiantes, id_estudiante)
    if estudiante is None:
        error(f"El estudiante con ID {id_estudiante} no existe en el sistema.")
        return
    calificaciones_estudiante = [cal for cal in calificaciones if cal[0][1] == id_estudiante]
    if calificaciones_estudiante:
        subtitulo(f"Boletín de Calificaciones: {estudiante['nombre']} {estudiante['apellido']}")
        print(f"  {'MATERIA':<25} | {'NOTA':<6} | {'ESTADO':<10}")
        separador()
        for cal in calificaciones_estudiante:
            id_materia = cal[0][0]
            nota = cal[1]
            materia = buscar_materia(materias, id_materia)
            nombre_m = materia['nombre'] if isinstance(materia, dict) else "Desconocida"
            estado = "Aprobado" if nota >= 4.0 else "Reprobado"
            print(f"  {nombre_m:<25} | {nota:<6.1f} | {estado:<10}")
        separador()
    else:
        alerta(f"El estudiante {estudiante['nombre']} {estudiante['apellido']} no tiene calificaciones registradas.")