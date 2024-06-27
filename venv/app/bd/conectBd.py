import os
from sqlalchemy import Engine, create_engine, text          # text : Permite ejecutar querys de tipo sql
from sqlalchemy.exc import SQLAlchemyError
from decouple import config
from dotenv import load_dotenv

def db():
    #cargar las variables de entorno
    load_dotenv()
    result = ""

    #Datos para la bd
    db_type = os.getenv('DB_TYPE')
    usser = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    connectionString = f'{db_type}://{usser}:{password}@{host}:{port}/{db_name}'

    #Motor de Conexión
    engine = create_engine(connectionString)
    #Connectar
    connection = engine.connect()

    #Probar la conección a la base de datos
    query = 'SELECT * FROM FichaTec;'

    try:
        cnx = connection.execute(text(query))
        #if result.scalar() == 1:
        #for i in result:
        #    print(i)
        return cnx
    except Exception as e:
        return print(f'error : {e}')
#pruebas con couple
def jeje():
    print(config('DB_USER'))
    
#db()