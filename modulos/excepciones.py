class ErrorGestion(Exception):
    """Error base de las operaciones del sistema académico."""


class RegistroNoEncontrado(ErrorGestion):
    """El estudiante, materia o calificación solicitado no existe."""


class RegistroDuplicado(ErrorGestion):
    """Ya existe un registro con ese ID, legajo o clave."""


class DatoInvalido(ErrorGestion):
    """El dato ingresado no cumple el formato o rango esperado."""
