def mostrar_menu_principal(rol):
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Estudiantes")
    print("2. Materias")
    print("3. Calificaciones")
    print("4. Estadísticas")
    print("5. Salir")

def sub_menu_estudiantes(rol):
    print("\n--- GESTIÓN DE ESTUDIANTES ---")
    if rol == "admin":
        print("1. Agregar estudiante")
        print("2. Consultar estudiante")
        print("3. Eliminar estudiante")
        print("4. Actualizar estudiante")
        print("5. Volver al menú principal")
    else:
        print("1. Ver mis datos académicos")
        print("2. Volver al menú principal")


def sub_menu_materias(rol):
    print("\n--- GESTIÓN DE MATERIAS ---")
    if rol == "admin":
        print("1. Agregar materia")
        print("2. Consultar materia")
        print("3. Eliminar materia")
        print("4. Actualizar materia")
        print("5. Volver al menú principal")
    else:
        print("1. Consultar materias disponibles")
        print("2. Volver al menú principal")


def sub_menu_calificaciones(rol):
    print("\n--- GESTIÓN DE CALIFICACIONES ---")
    if rol == "admin":
        print("1. Registrar calificación")
        print("2. Modificar calificación")
        print("3. Eliminar calificación")
        print("4. Consultar historial de estudiante")
        print("5. Volver al menú principal")
    else:
        print("1. Consultar mis calificaciones")
        print("2. Volver al menú principal")