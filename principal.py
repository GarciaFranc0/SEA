import datos
import modulos

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
                if modulos.login_admin():
                    rol_usuario = "admin"
                    autenticado = True
            case "2":
                exito, id_est = modulos.login_estudiante(datos.estudiantes)
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
        modulos.mostrar_menu_principal(rol_usuario)
        opcion = input("\nSeleccione una opción: ").strip()
        
        match opcion:
            case "1":
                modulos.sub_menu_estudiantes(rol_usuario)
                sub_op = input("Seleccione sub-opción: ").strip()
                
                if rol_usuario == "admin":
                    match sub_op:
                        case "1":
                            id_a = modulos.pedir_entero("ID Estudiante: ")
                            nom = input("Nombre: ").strip()
                            ape = input("Apellido: ").strip()
                            leg = modulos.pedir_entero("Legajo: ")
                            modulos.agregar_estudiante(datos.estudiantes, id_a, nom, ape, leg)
                        case "2":
                            id_a = modulos.pedir_entero("ID a consultar: ")
                            modulos.mostrar_estudiantes(datos.estudiantes, id_a)
                        case "3":
                            id_a = modulos.pedir_entero("ID a eliminar: ")
                            modulos.eliminar_estudiante(datos.estudiantes, id_a)
                        case "4":
                            id_a = modulos.pedir_entero("ID a actualizar: ")
                            nom = input("Nuevo Nombre: ").strip()
                            ape = input("Nuevo Apellido: ").strip()
                            leg = modulos.pedir_entero("Nuevo Legajo: ")
                            modulos.actualizar_estudiante(datos.estudiantes, id_a, nom, ape, leg)
                else:
                    if sub_op == "1":
                        modulos.mostrar_estudiantes(datos.estudiantes, id_estudiante_sesion)

            case "2":
                modulos.sub_menu_materias(rol_usuario)
                sub_op = input("Seleccione sub-opción: ").strip()
                
                if rol_usuario == "admin":
                    match sub_op:
                        case "1":
                            id_m = modulos.pedir_entero("ID Materia: ")
                            nom_m = input("Nombre de la Materia: ").strip()
                            modulos.agregar_materia(datos.materias, id_m, nom_m)
                        case "2":
                            id_m = modulos.pedir_entero("ID a consultar: ")
                            modulos.mostrar_materias(datos.materias, id_m)
                        case "3":
                            id_m = modulos.pedir_entero("ID a eliminar: ")
                            modulos.eliminar_materia(datos.materias, id_m)
                        case "4":
                            id_m = modulos.pedir_entero("ID a actualizar: ")
                            nom_m = input("Nuevo Nombre Materia: ").strip()
                            modulos.actualizar_materia(datos.materias, id_m, nom_m)
                else:
                    if sub_op == "1":
                        print("\n--- MATERIAS DISPONIBLES ---")
                        for id_m, m in datos.materias.items():
                            print(f"ID: {id_m} | Nombre: {m['nombre']}")

            case "3":
                modulos.sub_menu_calificaciones(rol_usuario)
                sub_op = input("Seleccione sub-opción: ").strip()
                
                if rol_usuario == "admin":
                    match sub_op:
                        case "1":
                            id_m = modulos.pedir_entero("ID Materia: ")
                            id_e = modulos.pedir_entero("ID Estudiante: ")
                            nota_input = input("Nota (0-10): ").strip()
                            if modulos.validar_nota(nota_input):
                                modulos.agregar_calificacion(datos.calificaciones, id_m, id_e, float(nota_input))
                            else:
                                print("Nota inválida.")
                        case "2":
                            id_m = modulos.pedir_entero("ID Materia: ")
                            id_e = modulos.pedir_entero("ID Estudiante: ")
                            nota_input = input("Nueva Nota (0-10): ").strip()
                            if modulos.validar_nota(nota_input):
                                modulos.actualizar_calificacion(datos.calificaciones, id_m, id_e, float(nota_input))
                            else:
                                print("Nota inválida.")
                        case "3":
                            id_m = modulos.pedir_entero("ID Materia: ")
                            id_e = modulos.pedir_entero("ID Estudiante: ")
                            modulos.eliminar_calificacion(datos.calificaciones, id_m, id_e)
                        case "4":
                            id_e = modulos.pedir_entero("ID Estudiante: ")
                            modulos.mostrar_calificaciones(datos.estudiantes, datos.materias, datos.calificaciones, id_e)
                else:
                    if sub_op == "1":
                        modulos.mostrar_calificaciones(datos.estudiantes, datos.materias, datos.calificaciones, id_estudiante_sesion)

            case "4":
                modulos.subtitulo("Reportes y Estadísticas Generales")
                if rol_usuario == "admin":
                    print("  [1] 📈 Promedio general por materia")
                    print("  [2] 📊 Porcentaje de aprobados por materia")
                    print("  [3] ⭐ Porcentaje de alumnos destacados (>=8.0)")
                    print("  [4] ↕️  Notas extremas del sistema")
                    print("  [5] 👤 Resumen académico completo por alumno")
                    sub_e = input("\nSeleccione reporte: ").strip()
                    
                    match sub_e:
                        case "1":
                            id_m = modulos.pedir_entero("ID Materia: ")
                            prom = modulos.promedio_materia(datos.calificaciones, id_m)
                            modulos.subtitulo(f"Promedio de la materia ID {id_m}: {prom:.2f}")
                        case "3":
                            porc_a = modulos.porcentaje_promedio_alto(datos.estudiantes, datos.calificaciones)
                            modulos.subtitulo(f"Alumnos con promedio alto (>= 8.0): {porc_a:.1f}%")
                        case "4":
                            ext = modulos.notas_extremas(datos.calificaciones)
                            modulos.subtitulo("Calificaciones Extremas del Sistema")
                            print(f"  🔻 Nota más baja: {ext[0]}")
                            print(f"  🔺 Nota más alta: {ext[1]}")
                            modulos.separador()
                        case "5":
                            id_e = modulos.pedir_entero("ID Estudiante: ")
                            res = modulos.estadistica_completa_estudiante(datos.estudiantes, datos.calificaciones, datos.materias, id_e)
                            print(f"Materias cursadas: {res['total']} | Promedio: {res['promedio']:.2f} | Máxima: {res['maxima']} | Mínima: {res['minima']}")
                else:
                    res = modulos.estadistica_completa_estudiante(datos.estudiantes, datos.calificaciones, datos.materias, id_estudiante_sesion)
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