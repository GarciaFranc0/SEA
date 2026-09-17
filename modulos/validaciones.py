import re


PATRON_EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
PATRON_LEGAJO = re.compile(r"^\d+$")
PATRON_NOTA = re.compile(r"^(?:10(?:\.0+)?|[0-9](?:\.[0-9]+)?)$")


def validar_email(email):
    """Devuelve True si el email tiene un formato valido."""
    return isinstance(email, str) and bool(PATRON_EMAIL.fullmatch(email.strip()))


def validar_legajo(legajo):
    """Devuelve True si el legajo contiene solo digitos y no esta vacio."""
    return not isinstance(legajo, bool) and bool(
        PATRON_LEGAJO.fullmatch(str(legajo).strip())
    )


def validar_nota(nota):
    """Devuelve True si la nota es numerica y esta entre 0 y 10."""
    if isinstance(nota, bool):
        return False
    return bool(PATRON_NOTA.fullmatch(str(nota).strip()))


def _valor_registro(registro, posicion, clave):
    """Obtiene un campo de un diccionario o una posicion de una secuencia."""
    if isinstance(registro, dict):
        return registro.get(clave)
    return registro[posicion]


def _valores(registros, posicion=None):
    """Obtiene valores directos o una columna de registros."""
    if posicion is None:
        return registros
    clave = {0: "id", 3: "legajo"}.get(posicion)
    return [_valor_registro(registro, posicion, clave) for registro in registros]


def existen_ids_duplicados(registros, posicion_id=0):
    """Devuelve True si hay IDs repetidos en una lista de registros."""
    ids = _valores(registros, posicion_id)
    return len(ids) != len(set(ids))


def existen_legajos_duplicados(registros, posicion_legajo=3):
    """Devuelve True si hay legajos repetidos en una lista de registros."""
    legajos = _valores(registros, posicion_legajo)
    return len(legajos) != len(set(legajos))


def ids_duplicados(registros, posicion_id=0):
    """Devuelve el conjunto de IDs que aparecen mas de una vez."""
    ids = _valores(registros, posicion_id)
    vistos = set()
    duplicados = set()
    for identificador in ids:
        if identificador in vistos:
            duplicados.add(identificador)
        vistos.add(identificador)
    return duplicados


def legajos_duplicados(registros, posicion_legajo=3):
    """Devuelve el conjunto de legajos que aparecen mas de una vez."""
    legajos = _valores(registros, posicion_legajo)
    vistos = set()
    duplicados = set()
    for legajo in legajos:
        if legajo in vistos:
            duplicados.add(legajo)
        vistos.add(legajo)
    return duplicados


def estudiantes_en_ambas_materias(inscriptos_materia_a, inscriptos_materia_b):
    """Devuelve los IDs de estudiantes inscriptos en ambas materias."""
    return set(inscriptos_materia_a).intersection(set(inscriptos_materia_b))


def estudiantes_solo_en_materia(inscriptos_materia_a, inscriptos_materia_b):
    """Devuelve los IDs inscriptos en A pero no en B."""
    return set(inscriptos_materia_a).difference(set(inscriptos_materia_b))

def pedir_entero(mensaje):
    #solicita un número entero al usuario y valida la entrada
    valido = False
    numero = 0
    while not valido:
        entrada = input(mensaje).strip()
        if entrada.isdigit():
            numero = int(entrada)
            valido = True
        else:
            print("Entrada inválida. Debe ingresar un número entero.")
    return numero

hay_ids_duplicados = existen_ids_duplicados
hay_legajos_duplicados = existen_legajos_duplicados
interseccion_estudiantes = estudiantes_en_ambas_materias
diferencia_estudiantes = estudiantes_solo_en_materia
