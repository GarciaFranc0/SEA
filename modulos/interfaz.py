ANCHO = 55

def titulo(texto):
    """Imprime un título destacado entre líneas dobles."""
    print("\n" + "═" * ANCHO)
    print(f"  {texto.upper().center(ANCHO - 4)}")
    print("═" * ANCHO)

def subtitulo(texto):
    """Imprime un subtítulo entre líneas simples."""
    print("\n" + "─" * ANCHO)
    print(f"📌 {texto}")
    print("─" * ANCHO)

def exito(texto):
    """Imprime un mensaje de éxito."""
    print(f"\n✔ [ÉXITO] {texto}")

def error(texto):
    """Imprime un mensaje de error."""
    print(f"\n✖ [ERROR] {texto}")

def alerta(texto):
    """Imprime un mensaje de alerta."""
    print(f"\n⚠️  [ALERTA] {texto}")

def separador():
    """Imprime una línea separadora."""
    print("─" * ANCHO)