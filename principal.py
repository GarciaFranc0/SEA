import 
# Funciones

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

def buscar_estudiante(estudiantes, id_alumno):
    resultado = None
    for estudiante in estudiantes:
        if estudiante[0] == id_alumno:
            resultado = estudiante       
    if resultado is None:
        resultado = "El estudiante no existe."
        
    return resultado

def buscar_materia(materias, id_materia):
    resultado = None
    for materia in materias:
        if materia[0] == id_materia:
            resultado = materia            
    if resultado == None:
        resultado = "La materia no existe."        
    return resultado

def buscar_calificacion(calificaciones, id_materia, id_estudiante):
    resultado = None
    for calificacion in calificaciones:
        if calificacion[0] == id_materia and calificacion[1] == id_estudiante:
            resultado = calificacion
    if resultado == None:
        resultado = "La calificación no existe."
    return resultado

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

def porcentaje_aprobados(id_materia):
    calificaciones_materia = [cal[2] for cal in calificaciones if cal[0] == id_materia]
    if calificaciones_materia:
        aprobados = len([cal for cal in calificaciones_materia if cal >= 4])
        porcentaje = (aprobados / len(calificaciones_materia)) * 100
        print(f"El porcentaje de estudiantes aprobados en la materia {materias[id_materia-1][1]} es: {porcentaje}%")
    else:
        print("No hay calificaciones registradas para esta materia.")

def mostrar_menu():
    print("1. Estudiantes")
    print("2. Materias")
    print("3. Calificaciones")
    print("4. Salir")

def sub_menu_estudiantes():
    print("1. Agregar estudiante")
    print("2. Mostrar estudiante")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Actualizar estudiante")
    print("6. Calcular promedio de estudiante")
    print("7. Volver al menú principal")

def sub_menu_materias():
    print("1. Agregar materia")
    print("2. Mostrar materia")
    print("3. Buscar materia")
    print("4. Eliminar materia")
    print("5. Actualizar materia")
    print("6. Porcentaje de aprobados en materia")
    print("7. Volver al menú principal")

def sub_menu_calificaciones():
    print("1. Agregar calificación")
    print("2. Mostrar calificaciones de estudiante")
    print("3. Buscar calificación")
    print("4. Eliminar calificación")
    print("5. Actualizar calificación")
    print("6. Volver al menú principal")

def login_admin():
    valido = False
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario == "admin" and contrasena == "admin":
        print("Inicio de sesión exitoso.")
        valido = True
    else:
        print("Usuario o contraseña incorrectos.")
        cont = 0
        while valido == False and cont < 5:
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            if usuario == "admin" and contrasena == "admin":
                print("Inicio de sesión exitoso.")
                valido = True
            else:
                print("Usuario o contraseña incorrectos.")
                cont += 1
    return valido

def login_estudiante():
    legajo = input("Ingrese su número de legajo: ")
    valido = False
    if legajo in [str(estudiante[3]) for estudiante in estudiantes]:
        print("Inicio de sesión exitoso.")
        valido = True
    else:
        print("Legajo incorrecto.")
        cont = 0
        while valido == False and cont < 5:
            legajo = input("Ingrese su número de legajo: ")
            if legajo in [str(estudiante[3]) for estudiante in estudiantes]:
                print("Inicio de sesión exitoso.")
                valido = True
            else:
                print("Legajo incorrecto.")
                cont += 1

# Matrices de entidades

# Menu principal
print("Bienvenido al sistema de gestión de estudiantes y materias.")


