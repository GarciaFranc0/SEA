import datos
import modulos

# Menu principal
print("Bienvenido al sistema de gestión de estudiantes y materias.")
rol = input("Ingrese su rol (admin/estudiante): ").strip().lower()
if rol == "admin":
    modulos.login_admin()
elif rol == "estudiante":
    modulos.login_estudiante()
else:
    print("Rol no válido.")