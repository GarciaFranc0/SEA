def login_admin():
    valido = False
    intentos = 0
    max_intentos = 3
    while not valido and intentos < max_intentos:
        usuario = input("Ingrese su nombre de usuario: ").strip()
        contrasena = input("Ingrese su contraseña: ").strip()
        if usuario == "admin" and contrasena == "admin":
            print("Inicio de sesión exitoso como Administrador.")
            valido = True
        else:
            intentos += 1
            intentos_restantes = max_intentos - intentos
            if intentos_restantes > 0:
                print(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos_restantes}")
            else:
                print("Se ha alcanzado el límite máximo de intentos.")              
    return valido

def login_estudiante(estudiantes):
    valido = False
    intentos = 0
    max_intentos = 3
    legajos_validos = list(map(lambda e: str(e[3]), estudiantes))
    while not valido and intentos < max_intentos:
        legajo = input("Ingrese su número de legajo: ").strip()
        if legajo in legajos_validos:
            print("Inicio de sesión exitoso como Estudiante.")
            valido = True
        else:
            intentos += 1
            intentos_restantes = max_intentos - intentos
            if intentos_restantes > 0:
                print(f"Legajo incorrecto. Intentos restantes: {intentos_restantes}")
            else:
                print("Se ha alcanzado el límite máximo de intentos.")          
    return valido