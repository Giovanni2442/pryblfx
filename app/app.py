#Alimentar base de datos#

#crate_engine   : Crea el motor hacia la conección a la base de datos
#text           : permite escribir consultas de tipo sql

import os                                                   # sqlalchemy : permita la concexión a la base de datos
from sqlalchemy import Engine, create_engine, text          # text : Permite ejecutar querys de tipo sql
import pandas as pd                                         # Biblioteca para leer archivos excel
from sqlalchemy.exc import SQLAlchemyError
import components as cm

# ---- Conexión a la base de datos  ----
def db():
    result = ""
    #Datos para la bd
    db_type = 'mysql+pymysql'
    usser = 'root'
    password = '2442'
    host = 'localhost'
    port = '3306'
    db_name = 'dbIngBF'
    connectionString = f'{db_type}://{usser}:{password}@{host}:{port}/{db_name}'

    #Motor de Conexión
    engine = create_engine(connectionString)
    #Connectar
    connection = engine.connect()

    #Probar la conección a la base de datos
    try:
        result = connection.execute(text("SELECT 1"))
        if result.scalar() == 1:
            return connection
    except Exception as e:
        return print(f'error : {e}')
    
#Lectura del excel
def read():
    #--Leer archivo desde la ruta --
    dir = 'c:/Users/gumrt/Desktop/ProyctIng/app/excelData/Data.xlsx'
    data = pd.read_excel(dir,header=None)                           #DESDE PANDAS INVOCAR LA FUNCION DE LECTURA
    #current_directory = os.path.dirname(__file__) Verifica el path
    
    #print(data)
    matrix = data.values
    print(matrix[0][0])

    #-Pruebas-
    #gnrlFilCal = 5
    #data_fila = data.iloc[:,gnrlFilCal]

    #-Especificar Columnas
    '''
    FichaTec
        id_codProduct
        cliente
        fecha_Elav
        fecha_Rev
        producto
    '''

    # --- CLASE ENCAPSULADA ATRIBUTOS ---
         #tabla FichaTecnica
    #data.iloc[columna:Fila] : Sirve para recorrer tablas y columnas de excel por medio de indices

    column = 2      #Comienzo de datos en columna 2 (CORREGIR : hacerlo con etiquetas)
    idProduct = data.iloc[column:,8] #Todos los datos apartir de la columna 2 y la fila 8 del indice
    cliente = data.iloc[column:,6]
    fechaElv = "N/A"
    fecha_Rev = data.iloc[column:,2]
    
   
    for c,f in data.iloc[column:].iterrows(): #Recorre las filas 
        try:
            with db() as connection:
                connection.execute(text(addFichTec(data,c)))  #text : Ejecuta consultas sql
                connection.commit()  # Confirmar la transacción
                print("Insert successful")
        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")

def test():
    dir = 'c:/Users/gumrt/Desktop/ProyctIng/app/excelData/Data.xlsx'
    data = pd.read_excel(dir,header=None)
    clmn = 2
    etiquetadoRefilado =  data.iloc[2:,119]
    print(etiquetadoRefilado)

    '''
    for c,f in data.iloc[clmn:].iterrows():
        try:
            with db() as connection:
                insertQuery = f"""
                    INSERT INTO FichaTec(id_codProduct, cliente, fecha_Elav, fecha_Rev, producto)
                    VALUES('{data[8][c]}', '{data[6][c]}', 'N/A', '{data[2][c]}', '{data[7][c]}')
                """
                connection.execute(text(insertQuery))
                connection.commit()  # Confirmar la transacción
                print("Insert successful")
        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")
       # pr1 = f[]'''
    
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