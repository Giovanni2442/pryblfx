import re
from tableAtributes import *    #Acceder a los tributos de cada Tabla

def vrfIsletter(*args):
    patron = re.compile('^[a-zA-Z. ]+$')
    return any(bool(patron.fullmatch(arg)) for arg in args)

def pru():
    pr = atrLaminado.je()
    print(pr.prueba)
    
pru()