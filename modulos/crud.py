from .interfaz import subtitulo, exito, separador, alerta
from .validaciones import validar_legajo, validar_nota
from .excepciones import RegistroNoEncontrado, RegistroDuplicado, DatoInvalido


def _buscar_registro(registros, valor, posicion=0, indice=0):
    if indice >= len(registros):
        return None
    if registros[indice][posicion] == valor:
        return registros[indice]
    return _buscar_registro(registros, valor, posicion, indice + 1)


def buscar_estudiante(estudiantes, id_alumno):
    return _buscar_registro(estudiantes, id_alumno)

def buscar_materia(materias, id_materia):
    return _buscar_registro(materias, id_materia)

def buscar_calificacion(calificaciones, id_materia, id_estudiante):
    return _buscar_registro(calificaciones, (id_materia, id_estudiante))


def _obtener_estudiante(estudiantes, id_alumno):
    estudiante = buscar_estudiante(estudiantes, id_alumno)
    if estudiante is None:
        raise RegistroNoEncontrado(f"El estudiante con ID {id_alumno} no existe.")
    return estudiante

def _obtener_materia(materias, id_materia):
    materia = buscar_materia(materias, id_materia)
    if materia is None:
        raise RegistroNoEncontrado(f"La materia con ID {id_materia} no existe.")
    return materia

def _obtener_calificacion(calificaciones, id_materia, id_estudiante):
    calificacion = buscar_calificacion(calificaciones, id_materia, id_estudiante)
    if calificacion is None:
        raise RegistroNoEncontrado(f"No existe calificación del estudiante {id_estudiante} en la materia {id_materia}.")
    return calificacion

def _validar_legajo(estudiantes, legajo, id_alumno):
    if not validar_legajo(legajo):
        raise DatoInvalido("El legajo debe contener solo dígitos.")
    for otro in estudiantes:
        if otro[3] == int(legajo) and otro[0] != id_alumno:
            raise RegistroDuplicado(f"El legajo {legajo} ya pertenece a otro estudiante.")

def _validar_nota(nota):
    if not validar_nota(nota):
        raise DatoInvalido("La nota debe estar entre 0 y 10.")


def agregar_estudiante(estudiantes, id_alumno, nombre, apellido, legajo):
    if buscar_estudiante(estudiantes, id_alumno) is not None:
        raise RegistroDuplicado(f"Ya existe un estudiante con ID {id_alumno}.")
    _validar_legajo(estudiantes, legajo, id_alumno)
    estudiantes.append([id_alumno, nombre, apellido, int(legajo)])
    exito("Estudiante registrado con éxito.")

def agregar_materia(materias, id_materia, nombre_materia):
    if buscar_materia(materias, id_materia) is not None:
        raise RegistroDuplicado(f"Ya existe una materia con ID {id_materia}.")
    materias.append([id_materia, nombre_materia])
    exito("Materia registrada con éxito.")

def agregar_calificacion(estudiantes, materias, calificaciones, id_materia, id_estudiante, nota):
    _validar_nota(nota)
    _obtener_estudiante(estudiantes, id_estudiante)
    _obtener_materia(materias, id_materia)
    if buscar_calificacion(calificaciones, id_materia, id_estudiante) is not None:
        raise RegistroDuplicado("La calificación ya existe. Use la opción de modificar.")
    calificaciones.append([(id_materia, id_estudiante), nota])
    exito("Calificación registrada con éxito.")


def eliminar_estudiante(estudiantes, calificaciones, id_alumno):
    estudiantes.remove(_obtener_estudiante(estudiantes, id_alumno))
    calificaciones[:] = list(filter(lambda calificacion: calificacion[0][1] != id_alumno, calificaciones))
    exito("Estudiante eliminado correctamente.")

def eliminar_materia(materias, calificaciones, id_materia):
    materias.remove(_obtener_materia(materias, id_materia))
    calificaciones[:] = list(filter(lambda calificacion: calificacion[0][0] != id_materia, calificaciones))
    exito("Materia eliminada correctamente.")

def eliminar_calificacion(calificaciones, id_materia, id_estudiante):
    calificaciones.remove(_obtener_calificacion(calificaciones, id_materia, id_estudiante))
    exito("Calificación eliminada correctamente.")


def actualizar_estudiante(estudiantes, id_alumno, nuevo_nombre, nuevo_apellido, nuevo_legajo):
    estudiante = _obtener_estudiante(estudiantes, id_alumno)
    _validar_legajo(estudiantes, nuevo_legajo, id_alumno)
    estudiante[1] = nuevo_nombre
    estudiante[2] = nuevo_apellido
    estudiante[3] = int(nuevo_legajo)
    exito("Estudiante actualizado correctamente.")

def actualizar_materia(materias, id_materia, nueva_materia):
    _obtener_materia(materias, id_materia)[1] = nueva_materia
    exito("Materia actualizada correctamente.")

def actualizar_calificacion(calificaciones, id_materia, id_estudiante, nueva_calificacion):
    _validar_nota(nueva_calificacion)
    _obtener_calificacion(calificaciones, id_materia, id_estudiante)[1] = nueva_calificacion
    exito("Calificación actualizada correctamente.")


def mostrar_estudiantes(estudiantes, id_alumno):
    estudiante = _obtener_estudiante(estudiantes, id_alumno)
    subtitulo("Información del Estudiante")
    print(f"  {'ID':<6} | {'NOMBRE Y APELLIDO':<25} | {'LEGAJO':<10}")
    separador()
    nombre_completo = f"{estudiante[1]} {estudiante[2]}"
    print(f"  {estudiante[0]:<6} | {nombre_completo:<25} | {estudiante[3]:<10}")
    separador()

def mostrar_materias(materias, id_materia):
    materia = _obtener_materia(materias, id_materia)
    subtitulo("Información de la Materia")
    print(f"  {'ID':<6} | {'NOMBRE':<25}")
    separador()
    print(f"  {materia[0]:<6} | {materia[1]:<25}")
    separador()

def mostrar_calificaciones(estudiantes, materias, calificaciones, id_estudiante):
    estudiante = _obtener_estudiante(estudiantes, id_estudiante)
    calificaciones_estudiante = [cal for cal in calificaciones if cal[0][1] == id_estudiante]
    if not calificaciones_estudiante:
        alerta(f"El estudiante {estudiante[1]} {estudiante[2]} no tiene calificaciones registradas.")
        return
    subtitulo(f"Boletín de Calificaciones: {estudiante[1]} {estudiante[2]}")
    print(f"  {'MATERIA':<25} | {'NOTA':<6} | {'ESTADO':<10}")
    separador()
    for (id_materia, _), nota in calificaciones_estudiante:
        materia = buscar_materia(materias, id_materia)
        nombre_m = materia[1] if materia is not None else "Desconocida"
        estado = "Aprobado" if nota >= 4.0 else "Reprobado"
        print(f"  {nombre_m:<25} | {nota:<6.1f} | {estado:<10}")
    separador()
