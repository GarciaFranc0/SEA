import csv
import json
import os

from .interfaz import error, alerta
from .validaciones import valores_duplicados, validar_nota


CARPETA_DATOS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datos")
RUTA_ESTUDIANTES = os.path.join(CARPETA_DATOS, "estudiantes.csv")
RUTA_MATERIAS = os.path.join(CARPETA_DATOS, "materias.csv")
RUTA_CALIFICACIONES = os.path.join(CARPETA_DATOS, "calificaciones.json")

ENCABEZADO_ESTUDIANTES = ["id", "nombre", "apellido", "legajo"]
ENCABEZADO_MATERIAS = ["id", "nombre"]


def _a_entero(valor, campo):
    """Convierte un valor a entero o lanza ValueError con un mensaje claro."""
    try:
        return int(valor)
    except (ValueError, TypeError):
        raise ValueError(f"el campo '{campo}' debe ser un número entero (valor: '{valor}')") from None


def _texto_no_vacio(valor, campo):
    """Devuelve el texto sin espacios o lanza ValueError si está vacío."""
    texto = str(valor).strip()
    if not texto:
        raise ValueError(f"el campo '{campo}' no puede estar vacío")
    return texto


def _convertir_estudiante(fila):
    if len(fila) != len(ENCABEZADO_ESTUDIANTES):
        raise ValueError(f"se esperaban {len(ENCABEZADO_ESTUDIANTES)} columnas y hay {len(fila)}")
    id_alumno, nombre, apellido, legajo = fila
    return [
        _a_entero(id_alumno, "id"),
        _texto_no_vacio(nombre, "nombre"),
        _texto_no_vacio(apellido, "apellido"),
        _a_entero(legajo, "legajo"),
    ]


def _convertir_materia(fila):
    if len(fila) != len(ENCABEZADO_MATERIAS):
        raise ValueError(f"se esperaban {len(ENCABEZADO_MATERIAS)} columnas y hay {len(fila)}")
    id_materia, nombre = fila
    return [_a_entero(id_materia, "id"), _texto_no_vacio(nombre, "nombre")]


def _convertir_calificacion(item):
    if not isinstance(item, dict):
        raise ValueError("cada calificación debe ser un objeto JSON")
    try:
        id_materia = _a_entero(item["id_materia"], "id_materia")
        id_estudiante = _a_entero(item["id_estudiante"], "id_estudiante")
        nota = item["nota"]
    except KeyError as campo:
        raise ValueError(f"falta el campo {campo}") from None
    if not isinstance(nota, (int, float)) or not validar_nota(nota):
        raise ValueError(f"la nota debe ser un número entre 0 y 10 (valor: {nota!r})")
    return [(id_materia, id_estudiante), nota]


def _leer_csv(ruta, encabezado, convertir):
    """Lee un CSV con encabezado; las filas inválidas se informan y se omiten."""
    registros = []
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        if next(lector, None) != encabezado:
            raise ValueError(f"encabezado inválido, se esperaba: {','.join(encabezado)}")
        for numero_linea, fila in enumerate(lector, start=2):
            if not fila:
                continue
            try:
                registros.append(convertir(fila))
            except ValueError as e:
                alerta(f"{os.path.basename(ruta)}, línea {numero_linea} ignorada: {e}.")
    return registros


def _leer_estudiantes(ruta):
    estudiantes = _leer_csv(ruta, ENCABEZADO_ESTUDIANTES, _convertir_estudiante)
    repetidos = valores_duplicados(estudiantes)
    if repetidos:
        raise ValueError(f"IDs de estudiante repetidos: {sorted(repetidos)}")
    repetidos = valores_duplicados(estudiantes, 3)
    if repetidos:
        raise ValueError(f"legajos repetidos: {sorted(repetidos)}")
    return estudiantes


def _leer_materias(ruta):
    materias = _leer_csv(ruta, ENCABEZADO_MATERIAS, _convertir_materia)
    repetidos = valores_duplicados(materias)
    if repetidos:
        raise ValueError(f"IDs de materia repetidos: {sorted(repetidos)}")
    return materias


def _leer_calificaciones(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = json.load(archivo)
    if not isinstance(contenido, list):
        raise ValueError("el archivo debe contener una lista de calificaciones")
    calificaciones = []
    for posicion, item in enumerate(contenido, start=1):
        try:
            calificaciones.append(_convertir_calificacion(item))
        except ValueError as e:
            alerta(f"{os.path.basename(ruta)}, calificación #{posicion} ignorada: {e}.")
    repetidos = valores_duplicados(calificaciones)
    if repetidos:
        raise ValueError(f"calificaciones repetidas (materia, estudiante): {sorted(repetidos)}")
    return calificaciones


def _escribir_csv(ruta, encabezado, registros):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)
        escritor.writerows(registros)


def _escribir_estudiantes(ruta, estudiantes):
    _escribir_csv(ruta, ENCABEZADO_ESTUDIANTES, estudiantes)


def _escribir_materias(ruta, materias):
    _escribir_csv(ruta, ENCABEZADO_MATERIAS, materias)


def _escribir_calificaciones(ruta, calificaciones):
    contenido = [
        {"id_materia": clave[0], "id_estudiante": clave[1], "nota": nota}
        for clave, nota in calificaciones
    ]
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, ensure_ascii=False, indent=2)


def _guardar(ruta, escribir, registros):
    """Escribe en un archivo temporal y luego lo reemplaza, para no dejar archivos a medio escribir."""
    nombre = os.path.basename(ruta)
    ruta_temporal = ruta + ".tmp"
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        escribir(ruta_temporal, registros)
        os.replace(ruta_temporal, ruta)
        return True
    except PermissionError:
        error(f"Sin permisos para escribir '{nombre}'. Los cambios no se guardaron.")
    except OSError as e:
        error(f"No se pudo guardar '{nombre}': {e.strerror}.")
    except (TypeError, ValueError) as e:
        error(f"Los datos de '{nombre}' no se pudieron convertir al formato del archivo: {e}.")
    if os.path.exists(ruta_temporal):
        os.remove(ruta_temporal)
    return False


def _cargar(ruta, leer, escribir, por_defecto):
    """Lee un archivo de datos; si falla, informa el motivo y devuelve los datos por defecto."""
    nombre = os.path.basename(ruta)
    try:
        return leer(ruta)
    except FileNotFoundError:
        alerta(f"No se encontró '{nombre}'. Se crea con los datos iniciales.")
        _guardar(ruta, escribir, por_defecto)
    except PermissionError:
        error(f"Sin permisos para leer '{nombre}'. Se usan los datos iniciales.")
    except json.JSONDecodeError as e:
        error(f"'{nombre}' no es un JSON válido (línea {e.lineno}, columna {e.colno}). Se usan los datos iniciales.")
    except UnicodeDecodeError:
        error(f"'{nombre}' no está codificado en UTF-8. Se usan los datos iniciales.")
    except (ValueError, csv.Error) as e:
        error(f"'{nombre}' tiene un formato inválido: {e}. Se usan los datos iniciales.")
    except OSError as e:
        error(f"No se pudo abrir '{nombre}': {e.strerror}. Se usan los datos iniciales.")
    return por_defecto


def cargar_datos(estudiantes, materias, calificaciones):
    """Reemplaza el contenido de las listas con lo guardado en los archivos."""
    estudiantes[:] = _cargar(RUTA_ESTUDIANTES, _leer_estudiantes, _escribir_estudiantes, estudiantes)
    materias[:] = _cargar(RUTA_MATERIAS, _leer_materias, _escribir_materias, materias)
    calificaciones[:] = _cargar(RUTA_CALIFICACIONES, _leer_calificaciones, _escribir_calificaciones, calificaciones)


def guardar_datos(estudiantes, materias, calificaciones):
    """Guarda las tres listas en sus archivos. Devuelve True si todo se guardó."""
    resultados = [
        _guardar(RUTA_ESTUDIANTES, _escribir_estudiantes, estudiantes),
        _guardar(RUTA_MATERIAS, _escribir_materias, materias),
        _guardar(RUTA_CALIFICACIONES, _escribir_calificaciones, calificaciones),
    ]
    return all(resultados)
