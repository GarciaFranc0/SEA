# main.py
import datos
import modulos.login as auth
import modulos.menus as menus
import modulos.crud as crud
import modulos.estadisticas as est
from modulos.validaciones import validar_nota, pedir_entero

def ejecutar_sistema():
    print("==================================================")
    print(" BIENVENIDO AL SISTEMA DE GESTIÓN ACADÉMICA ")
    print("==================================================")
    
    # 1. AUTENTICACIÓN
    rol_usuario = ""
    id_estudiante_sesion = None
    autenticado = False
    salir_programa = False
    
    while not autenticado and not salir_programa:
        print("\nSeleccione tipo de acceso:")
        print("1. Administrador\n2. Estudiante\n3. Salir del programa")
        opcion_login = input("Opción: ").strip()
        
        match opcion_login:
            case "1":
                if auth.login_admin():
                    rol_usuario = "admin"
                    autenticado = True
            case "2":
                exito, id_est = auth.login_estudiante(datos.estudiantes)
                if exito:
                    rol_usuario = "estudiante"
                    id_estudiante_sesion = id_est
                    autenticado = True
            case "3":
                print("Gracias por utilizar el sistema. ¡Hasta luego!")
                salir_programa = True
            case _:
                print("Opción inválida. Seleccione 1, 2 o 3.")

    # 2. BUCLE PRINCIPAL DE NAVEGACIÓN
    sistema_activo = autenticado
    while sistema_activo:
        menus.mostrar_menu_principal(rol_usuario)
        opcion = input("\nSeleccione una opción: ").strip()
        
        match opcion:
            case "1":
                menus.sub_menu_estudiantes(rol_usuario)
                sub_op = input("Seleccione sub-opción: ").strip()
                
                if rol_usuario == "admin":
                    match sub_op:
                        case "1":
                            id_a = pedir_entero("ID Estudiante: ")
                            nom = input("Nombre: ").strip()
                            ape = input("Apellido: ").strip()
                            leg = pedir_entero("Legajo: ")
                            crud.agregar_estudiante(datos.estudiantes, id_a, nom, ape, leg)
                        case "2":
                            id_a = pedir_entero("ID a consultar: ")
                            crud.mostrar_estudiantes(datos.estudiantes, id_a)
                        case "3":
                            id_a = pedir_entero("ID a eliminar: ")
                            crud.eliminar_estudiante(datos.estudiantes, id_a)
                        case "4":
                            id_a = pedir_entero("ID a actualizar: ")
                            nom = input("Nuevo Nombre: ").strip()
                            ape = input("Nuevo Apellido: ").strip()
                            leg = pedir_entero("Nuevo Legajo: ")
                            crud.actualizar_estudiante(datos.estudiantes, id_a, nom, ape, leg)
                else:
                    if sub_op == "1":
                        crud.mostrar_estudiantes(datos.estudiantes, id_estudiante_sesion)

            case "2":
                menus.sub_menu_materias(rol_usuario)
                sub_op = input("Seleccione sub-opción: ").strip()
                
                if rol_usuario == "admin":
                    match sub_op:
                        case "1":
                            id_m = pedir_entero("ID Materia: ")
                            nom_m = input("Nombre de la Materia: ").strip()
                            crud.agregar_materia(datos.materias, id_m, nom_m)
                        case "2":
                            id_m = pedir_entero("ID a consultar: ")
                            crud.mostrar_materias(datos.materias, id_m)
                        case "3":
                            id_m = pedir_entero("ID a eliminar: ")
                            crud.eliminar_materia(datos.materias, id_m)
                        case "4":
                            id_m = pedir_entero("ID a actualizar: ")
                            nom_m = input("Nuevo Nombre Materia: ").strip()
                            crud.actualizar_materia(datos.materias, id_m, nom_m)
                else:
                    if sub_op == "1":
                        print("\n--- MATERIAS DISPONIBLES ---")
                        for id_m, m in datos.materias.items():
                            print(f"ID: {id_m} | Nombre: {m['nombre']}")

            case "3":
                menus.sub_menu_calificaciones(rol_usuario)
                sub_op = input("Seleccione sub-opción: ").strip()
                
                if rol_usuario == "admin":
                    match sub_op:
                        case "1":
                            id_m = pedir_entero("ID Materia: ")
                            id_e = pedir_entero("ID Estudiante: ")
                            nota_input = input("Nota (0-10): ").strip()
                            if validar_nota(nota_input):
                                crud.agregar_calificacion(datos.calificaciones, id_m, id_e, float(nota_input))
                            else:
                                print("Nota inválida.")
                        case "2":
                            id_m = pedir_entero("ID Materia: ")
                            id_e = pedir_entero("ID Estudiante: ")
                            nota_input = input("Nueva Nota (0-10): ").strip()
                            if validar_nota(nota_input):
                                crud.actualizar_calificacion(datos.calificaciones, id_m, id_e, float(nota_input))
                            else:
                                print("Nota inválida.")
                        case "3":
                            id_m = pedir_entero("ID Materia: ")
                            id_e = pedir_entero("ID Estudiante: ")
                            crud.eliminar_calificacion(datos.calificaciones, id_m, id_e)
                        case "4":
                            id_e = pedir_entero("ID Estudiante: ")
                            crud.mostrar_calificaciones(datos.estudiantes, datos.materias, datos.calificaciones, id_e)
                else:
                    if sub_op == "1":
                        crud.mostrar_calificaciones(datos.estudiantes, datos.materias, datos.calificaciones, id_estudiante_sesion)

            case "4":
                print("\n--- REPORTES Y ESTADÍSTICAS ---")
                if rol_usuario == "admin":
                    print("1. Promedio general por materia")
                    print("2. Porcentaje de aprobados por materia")
                    print("3. Porcentaje de alumnos con promedio alto (>=8.0)")
                    print("4. Notas extremas del sistema (Mínima y Máxima)")
                    print("5. Resumen estadístico de un estudiante")
                    sub_e = input("Seleccione reporte: ").strip()
                    
                    match sub_e:
                        case "1":
                            id_m = pedir_entero("ID Materia: ")
                            prom = est.promedio_materia(datos.calificaciones, id_m)
                            print(f"Promedio general de la materia: {prom:.2f}")
                        case "2":
                            id_m = pedir_entero("ID Materia: ")
                            porc = est.porcentaje_aprobados(datos.calificaciones, id_m)
                            print(f"Porcentaje de aprobados: {porc:.2f}%")
                        case "3":
                            porc_a = est.porcentaje_promedio_alto(datos.estudiantes, datos.calificaciones)
                            print(f"Alumnos con promedio alto (>=8.0): {porc_a:.2f}%")
                        case "4":
                            ext = est.notas_extremas(datos.calificaciones)
                            print(f"Nota más baja: {ext[0]} | Nota más alta: {ext[1]}")
                        case "5":
                            id_e = pedir_entero("ID Estudiante: ")
                            res = est.estadistica_completa_estudiante(datos.estudiantes, datos.calificaciones, datos.materias, id_e)
                            print(f"Materias cursadas: {res['total']} | Promedio: {res['promedio']:.2f} | Máxima: {res['maxima']} | Mínima: {res['minima']}")
                else:
                    res = est.estadistica_completa_estudiante(datos.estudiantes, datos.calificaciones, datos.materias, id_estudiante_sesion)
                    print(f"\n--- TU RESUMEN ACADÉMICO ---")
                    print(f"Materias cursadas: {res['total']}")
                    print(f"Tu promedio general: {res['promedio']:.2f}")
                    print(f"Tu nota más alta: {res['maxima']}")
                    print(f"Tu nota más baja: {res['minima']}")

            case "5":
                print("\nCerrando sesión. ¡Gracias por usar el sistema!")
                sistema_activo = False
            case _:
                print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    ejecutar_sistema()