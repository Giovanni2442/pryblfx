import re

def vrfIsletter(*args):
    patron = re.compile('^[a-zA-Z. ]+$')
    return any(bool(patron.fullmatch(arg)) for arg in args)

# Ejemplo de uso
print(vrfIsletter("VEGETAL1", "VEGETAL 999"))  # Esto debe imprimir False
print(vrfIsletter("VEGETAL", "FRUTA"))          # Esto debe imprimir True
