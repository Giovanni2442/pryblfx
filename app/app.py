#Alimentar base de datos#

#crate_engine   : Crea el motor hacia la conección a la base de datos
#text           : permite escribir consultas de tipo sql
import pandas as pd
from sqlalchemy import text                                         # Biblioteca para leer archivos excel
from sqlalchemy.exc import SQLAlchemyError
from bd.conectBd import db
from filExcel.tableFilt import tableFilt as tblFil

#Lectura del excel
#--Leer archivo desde la ruta --
dir = 'app/excelData/Data.xlsx'    #Dirección del Archivo
data = pd.read_excel(dir,header=1)   

def read():
    
    # --- FUNCIONES DE VERIFICACIÓN ---
    #filtData(tblFil.tblFichTec)
    filtData(tblFil.tblVentas)
    #filtData(data,clmn,tblFil.pr1)
    #pru(data,clmn,tblFil.pr1)

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
def filtData(func):
    i = 0

    print("  \n-------TABLA-------  ")
    for c,row in data.iloc[:].iterrows(): #Recorre las filas
        table = func(row,c)

        #print("--",table)
        #Tabla fichaTec
        if table[0] != False:
            print("--",table)
        else :
            print(f'Error en la fila {table[1]}, por : {table[2]}')
            break
    print("\n")
        
#Modulo de Inserción a la tabla FichaTec

# data : especifica la fila
# c    : especifica las columnas
def addFichTec(data,c):
    insertQuery = f"""
        INSERT INTO FichaTec(id_codProduct, cliente, fecha_Elav, fecha_Rev, producto)
        VALUES('{data[8][c]}', '{data[6][c]}', 'N/A', '{data[2][c]}', '{data[7][c]}')
    """
    return insertQuery

def pru(dt,clmn,func):
    for c,row in dt.iloc[:].iterrows(): #Recorre las filas
        table = func(row)
        print(table)

read()
#test()