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
    #Verifica si hay un campo vacio
    def vrfNan(*args):                            # Se pasa 'n' cantidad de atributos a recorrer
        return any(pd.isna(arg) for arg in args)        #any() genera una lista donde verifica si existe algun 'nan' y devuelve un valor booleano

    #Verifica si el dato contiene solo letras
    def vrfIsletter(*args):
        patron = re.compile('^[a-zA-Z]')
        return any(bool(patron.match(arg) for arg in args))
    
    #Verifica la estructura del Producto
    def vrfEstrcProd(*args):
        patron = re.compile('^[a-zA-Z0-9]+$-')
        return any(bool(patron.match(arg)) for arg in args)
    
    #Verifica si el Codigo del printCard es correcto
    def vrfPrintCard(*args):
        patron = re.compile('^(?=.*\d{4,})[a-zA-Z0-9_-]+$')
        #res = bool(patron.match())
        return any(bool(patron.match(arg)) for arg in args)
    
    #Verifica las fechas de elavoración de las fichas tecnicas
    #dd/mm/yy
    def vrfFechas(*args):              #Dias                  /           Meses                 /        Años       
        patron = re.compile("^(0[1-9]|[12][0-9]|3[01])\s*(/|-)\s*(0[1-9]|1[0-2]|(\w{3}))\s*(/|-)\s*(\d{2}|\d{4})$")         #Validar las fechas deacuerdo con : [0-9][a-zA-Z][]
        return any(bool(patron.match(arg)) for arg in args)
   
    def vrfEstrcProd(*args):
        estructuras = ["LDPE","PET","BOPP"]
        estrctString = r'\b(?:' + '|'.join(estructuras) + r')\b'
        patron = re.compile(r'(' + estrctString + r'|\w+|\d|%)')
        return any(bool(patron.match(arg)) for arg in args)
    #   ----------------------------------
    #Tabla Ficha Tecnica    