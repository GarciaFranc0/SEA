# Funciones

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


