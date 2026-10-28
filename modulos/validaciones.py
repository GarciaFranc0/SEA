import re


PATRON_LEGAJO = re.compile(r"^\d+$")
PATRON_NOTA = re.compile(r"^(?:10(?:\.0+)?|[0-9](?:\.[0-9]+)?)$")


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


def valores_duplicados(registros, posicion=0):
    vistos = set()
    duplicados = set()
    return buscar_duplicados(registros, posicion, vistos, duplicados)


def buscar_duplicados(registros, posicion, vistos, duplicados):
    if len(registros) == 0:
        return duplicados
    else:
        valor = registros[0][posicion]

        if valor in vistos:
            duplicados.add(valor)

        vistos.add(valor)

        return buscar_duplicados(
            registros[1:], posicion, vistos, duplicados
        )


def pedir_entero(mensaje):
    #solicita un número entero al usuario y valida la entrada
    valido = False
    numero = 0
    while not valido:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
        else:
            if numero < 0:
                print("Entrada inválida. El número no puede ser negativo.")
            else:
                valido = True
    return numero

def pedir_nota(mensaje):
    #solicita una nota entre 0 y 10 y valida la entrada
    valido = False
    nota = 0.0
    while not valido:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("Entrada inválida. La nota debe ser un número (ej: 7 o 7.5).")
        else:
            if validar_nota(nota):
                valido = True
            else:
                print("Entrada inválida. La nota debe estar entre 0 y 10.")
    return nota

def pedir_opcion(mensaje, cantidad):
    #solicita una opción entre 1 y cantidad y repite hasta que sea válida
    opciones_validas = [str(numero) for numero in range(1, cantidad + 1)]
    opcion = input(mensaje).strip()
    while opcion not in opciones_validas:
        print(f"Opción inválida. Elija una opción entre 1 y {cantidad} e intente nuevamente.")
        opcion = input(mensaje).strip()
    return opcion

def pedir_texto(mensaje):
    #solicita un texto no vacío
    texto = input(mensaje).strip()
    while not texto:
        print("Entrada inválida. El campo no puede estar vacío.")
        texto = input(mensaje).strip()
    return texto
