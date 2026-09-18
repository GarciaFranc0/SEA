from modulos.interfaz import titulo, separador

def mostrar_menu_principal(rol):
    titulo("Menú Principal")
    print("  [1] 🎓 Gestión de Estudiantes")
    print("  [2] 📚 Gestión de Materias")
    print("  [3] 📝 Gestión de Calificaciones")
    print("  [4] 📊 Reportes y Estadísticas")
    print("  [5] 🚪 Salir del Sistema")
    separador()

def sub_menu_estudiantes(rol):
    titulo("Gestión de Estudiantes")
    if rol == "admin":
        print("  [1] ➕ Agregar estudiante")
        print("  [2] 🔍 Consultar estudiante")
        print("  [3] ❌ Eliminar estudiante")
        print("  [4] ✏️  Actualizar estudiante")
        print("  [5] ↩️  Volver al menú principal")
    else:
        print("  [1] 👤 Ver mis datos académicos")
        print("  [2] ↩️  Volver al menú principal")
    separador()

def sub_menu_materias(rol):
    titulo("Gestión de Materias")
    if rol == "admin":
        print("  [1] ➕ Agregar materia")
        print("  [2] 🔍 Consultar materia")
        print("  [3] ❌ Eliminar materia")
        print("  [4] ✏️  Actualizar materia")
        print("  [5] ↩️  Volver al menú principal")
    else:
        print("  [1] 📖 Consultar materias disponibles")
        print("  [2] ↩️  Volver al menú principal")
    separador()

def sub_menu_calificaciones(rol):
    titulo("Gestión de Calificaciones")
    if rol == "admin":
        print("  [1] ➕ Registrar calificación")
        print("  [2] ✏️  Modificar calificación")
        print("  [3] ❌ Eliminar calificación")
        print("  [4] 📋 Consultar historial de estudiante")
        print("  [5] ↩️  Volver al menú principal")
    else:
        print("  [1] 📑 Consultar mis calificaciones")
        print("  [2] ↩️  Volver al menú principal")
    separador()