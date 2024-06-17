#Alimentar base de datos#

#crate_engine   : Crea el motor hacia la conección a la base de datos
#text           : permite escribir consultas de tipo sql
import pandas as pd
from sqlalchemy import text                                         # Biblioteca para leer archivos excel
from sqlalchemy.exc import SQLAlchemyError
from bd.conectBd import db
from filExcel.tableFilt import tableFilt as tblFil

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
    
    filtData(data,clmn,tblFil.tblFichTec) 
    #tblFichTec(data,clmn)

    #Ejecutar query de Inserción
    '''for c in data.iloc[fila:].iterrows(): #Recorre las filas 
        try:
            with db() as conect:
                conect.execute(text(addFichTec(data,c)))  #text : Ejecuta consultas sql
                conect.commit()  # Confirmar la transacción
                print("Insert successful!")
        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")'''

#Filtra los datos por medio de valores de retorno
def filtData(dt,clmn,func):
    for c,row in dt.iloc[clmn:].iterrows(): #Recorre las filas
        table = func(row,clmn,c)

        #print(func(row,clmn,c))
        #Tabla fichaTec
        if table[0] != False:
            print("--",table)
        else :
            print(f'Error en la fila {table[1]}, por : {table[2]}')
            break
        
#Modulo de Inserción a la tabla FichaTec

# data : especifica la fila
# c    : especifica las columnas
def addFichTec(data,c):
    insertQuery = f"""
        INSERT INTO FichaTec(id_codProduct, cliente, fecha_Elav, fecha_Rev, producto)
        VALUES('{data[8][c]}', '{data[6][c]}', 'N/A', '{data[2][c]}', '{data[7][c]}')
    """
    return insertQuery

read()
#test()