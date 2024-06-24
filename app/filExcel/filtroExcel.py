import pandas as pd
import re 

#Acordeón :
# ^         : Ancla, asegura que la expreción busque desde el inicio de una cadena
# (?=.)     : Asegura la existencia de la cadena
# .*        : Evita saltos de linea y cualquier cosa proceda
# \d{4,}    : Coincide con cualquier digito, siempre y cuando cumpla el numero que se especifica en corchetes
# +         : Debe de haber uno o mas caracteres especificados en las llaves
# $         : Asegura que la coincidencia termine al final de la cadena
# r         : raw string, no cumple con caracteres especiales como : \n o \t

class filter():
    patron = ""
#  --- FILTRADORES DE DATOS ---    
    #Verifica si el campo esta lleno y no vacio
    # Retorna false si encuentra un campo vacio, de lo contrario es un True de que esta lleno el campo
    def vrfNan(*args):                            # Se pasa 'n' cantidad de atributos a recorrer
        return all( not pd.isna(arg) for arg in args)        #any() genera una lista donde verifica si existe algun 'nan' y devuelve un valor booleano

    #Verifica si el dato contiene solo letras
    def vrfIsletter(*args):
        patron = re.compile('^[a-zA-Z. ]+$')
        return all(all(bool(patron.fullmatch(item)) for item in arg) for arg in args) #itera por cada lista y despues por cada argumento de la lista
    
    #Verifica el Nombre del Cliente
    def vrfCliente(*args):
        patron = re.compile(r'^[a-zA-Z0-9_.() -]+$')
        return all(bool(patron.fullmatch(arg)) for arg in args)
    
    #Verifica si el Codigo del printCard es correcto
    def vrfPrintCard(*args):
        patron = re.compile('^(?=.*\d{4,})[a-zA-Z0-9_-]+$')
        return any(bool(patron.fullmatch(arg)) for arg in args)
    
    #Verifica las fechas de elavoración de las fichas tecnicas
    #dd/mm/yy
    def vrfFechas(*args):              #Dias                  /           Meses                 /        Años       
        patron = re.compile("^(0[1-9]|[12][0-9]|3[01])\s*(/|-)\s*(0[1-9]|1[0-2]|(\w{3}))\s*(/|-)\s*(\d{2}|\d{4})$")         #Validar las fechas deacuerdo con : [0-9][a-zA-Z][]
        return all(bool(patron.fullmatch(arg)) for arg in args)
   
    #Verifica la estructura del Producto
    def vrfEstrcProd(*args):
        estructuras = ["LDPE","PET","BOPP"]
        estrctString = r'\b(?:' + '|'.join(estructuras) + r')\b'
        patron = re.compile(r'(' + estrctString + r'|\w+%)')
        return any(bool(patron.fullmatch(arg)) for arg in args)

    def prEsctr(*args):
        patron = re.compile(
            r'^(PET|LDPE|BOPP)'                 # Coincide con PET, LDPE o BOPP
            r'(?:\([a-zA-Z]+\))?'               # Coincide opcionalmente con (BAJA)
            r'\s+'                              # Espacios después de PET, LDPE o BOPP
            r'\d+'                              # Coincide con uno o más dígitos
            r'\s*(GAUGES|GA|µ)'                 # Coincide con GAUGES, GA o µ
            r'(?:'                              # Inicio del grupo opcional para múltiples segmentos
            r'\s*/\s*'                          # Coincide con / rodeada de espacios
            r'[a-zA-Z]+'                        # Coincide con una secuencia de letras (material)
            r'(?:\([a-zA-Z]+\))?'               # Coincide opcionalmente con (BAJA)
            r'\s*\d+'                           # Coincide con uno o más dígitos
            r'\s*(GAUGES|GA|µ)'                 # Coincide con GAUGES, GA o µ
            r')*$'                              # Fin del grupo opcional y fin de la cadena
        )
        return all(bool(patron.fullmatch(arg)) for arg in args)

    def pru():
        patron = re.compile('^[a-zA-Z. ]+$')
        print(bool(patron.match("Hola. mundo")))       

pr = filter
#pr.pru()
    #   ----------------------------------
    #Tabla Ficha Tecnica    
