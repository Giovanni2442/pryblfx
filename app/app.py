#Alimentar base de datos#

#crate_engine   : Crea el motor hacia la conección a la base de datos
#text           : permite escribir consultas de tipo sql
import pandas as pd
from sqlalchemy import text                                         # Biblioteca para leer archivos excel
import components as cm
from sqlalchemy.exc import SQLAlchemyError
from bd.conectBd import db

#Lectura del excel
def read():
    #--Leer archivo desde la ruta --
    dir = 'c:/Users/gumrt/Desktop/ProyctIng/app/excelData/Data.xlsx'    #Dirección del Archivo
    data = pd.read_excel(dir,header=None)                               #DESDE PANDAS INVOCAR LA FUNCION DE LECTURA

    clmn = 2      #Comienzo de datos en columna 2 (CORREGIR : hacerlo con etiquetas)
    idProduct = data.iloc[clmn:,8] #Todos los datos apartir de la columna 2 y la fila 8 del indice
    cliente = data.iloc[clmn:,6]
    fechaElv = "N/A"
    fecha_Rev = data.iloc[clmn:,2]
    
    #filtData(data,clmn,tblFichTec)
    tblFichTec(data,clmn)

    #Ejecutar query de Inserción
    '''for c in data.iloc[fila:].iterrows(): #Recorre las filas 
        try:
            with db() as conect:
                conect.execute(text(addFichTec(data,c)))  #text : Ejecuta consultas sql
                conect.commit()  # Confirmar la transacción
                print("Insert successful!")
        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")'''


def filtData(dt,clmn,func):
    for c,row in dt.iloc[clmn:].iterrows(): #Recorre las filas
        filNan = (c-clmn)+1    #Especifica el lugar exacto donde se encuentra el dato vacio en Excel
        

        #Nota : Declarar las variables para cada tabla de la siguiente manera :
        # cliente = 9 # Se especifica el indice de la columna
        # row[cliente]
        #Tabla fichaTec
        codPrintCrd = row[8]      #Codigo del Producto
        cliente = row[9]
        fchaElav = row[2]
        product = row[7]

        func(row,clmn,c)


        '''#print("--",row[c:])
        if pd.isna(row[c]) :     #Identifica un NAN en el archivo de excel
            #print(f'Falta llenar en la fila {filNan}, columna {row[c]}')
            #break
            pass
        else:
            print(f'{codPoduct}  :  {row[9]} ----')
            pass'''

def verificarNan(*args):    # Se pasa 'n' cantidad de atributos a recorrer
    return any(pd.isna(arg) for arg in args)        #any() genera una lista donde verifica si existe algun 'nan' y devuelve un valor booleano

def tblFichTec(data,clmn):
    
    for c,row in data.iloc[clmn:].iterrows(): #Recorre las filas
        #Agregar Expreciónes regulares para cada fila
        codPrintCrd = row[8] 
        cliente = row[9]
        fchaElav = row[2]
        product = row[7]    

        filNan = (c-clmn)+1

        #print(f'{codPrintCrd}  : {cliente}')
           
        #Condificonales
        if verificarNan(codPrintCrd,cliente):
            print(f'Fallo en la fila : {filNan} , columna {clmn}')
            break
        else :
            print(f'{codPrintCrd}  :  {cliente}') 


    '''if pd.isna(codPrintCrd,cliente):
        #print(f'Falta llenar en la fila {filNan}')
        return 1 #banderin
    else :
        return f'{codPrintCrd} : {cliente} ----'''

    
#Modulo de Inserción a la tabla FichaTec
# data : especifica la fila
# c    : especifica las columnas
def addFichTec(data,c):
    insertQuery = f"""
        INSERT INTO FichaTec(id_codProduct, cliente, fecha_Elav, fecha_Rev, producto)
        VALUES('{data[8][c]}', '{data[6][c]}', 'N/A', '{data[2][c]}', '{data[7][c]}')
    """
    return insertQuery

def test():
    dir = 'c:/Users/gumrt/Desktop/ProyctIng/app/excelData/Data.xlsx'
    data = pd.read_excel(dir,header=None)
    clmn = 2
    etiquetadoRefilado =  data.iloc[2:,119]
    print(etiquetadoRefilado)

read()
#test()