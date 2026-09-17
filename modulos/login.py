from .validaciones import validar_legajo

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
    id_estudiante_logueado = None
    
    while not valido and intentos < max_intentos:
        legajo_input = input("Ingrese su número de legajo: ").strip()
        
        if validar_legajo(legajo_input):
            legajo_num = int(legajo_input)
            
            # Recorremos buscando la coincidencia con una bandera booleana
            i = 0
            encontrado = False
            while i < len(estudiantes) and not encontrado:
                if estudiantes[i].get("legajo") == legajo_num:
                    valido = True
                    encontrado = True
                    id_estudiante_logueado = estudiantes[i].get("id")
                    print(f"Inicio de sesión exitoso. ¡Bienvenido {estudiantes[i].get('nombre')}!")
                i += 1
        
        if not valido:
            intentos += 1
            intentos_restantes = max_intentos - intentos
            if intentos_restantes > 0:
                print(f"Legajo incorrecto o no encontrado. Intentos restantes: {intentos_restantes}")
            else:
                print("Se ha alcanzado el límite máximo de intentos.")         
                
    return (valido, id_estudiante_logueado)