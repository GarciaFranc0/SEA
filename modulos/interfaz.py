ANCHO = 55

def titulo(texto):
    print("\n" + "═" * ANCHO)
    print(f"  {texto.upper().center(ANCHO - 4)}")
    print("═" * ANCHO)

def subtitulo(texto):
    print("\n" + "─" * ANCHO)
    print(f"📌 {texto}")
    print("─" * ANCHO)

def exito(texto):
    print(f"\n✔ [ÉXITO] {texto}")

def error(texto):
    print(f"\n✖ [ERROR] {texto}")

def alerta(texto):
    print(f"\n⚠️  [ALERTA] {texto}")

def separador():
    print("─" * ANCHO)