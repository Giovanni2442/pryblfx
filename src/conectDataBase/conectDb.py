import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def db():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Datos para la bd obtenidos de las variables de entorno
    db_type = os.getenv('DB_TYPE')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    # Verificar que todas las variables se han cargado correctamente
    if not all([db_type, user, password, host, port, db_name]):
        return print("Error: Una o más variables de entorno no están configuradas correctamente.")
    
    connectionString = f'{db_type}://{user}:{password}@{host}:{port}/{db_name}'

    # Motor de Conexión
    try:
        engine = create_engine(connectionString)
        return engine.connect()
    except SQLAlchemyError as e:
        return print(f"Error al conectar con la base de datos: {e}")

# --- PRUEBAS QUERYS ---
def getAll():
    query = 'SELECT * FROM FichaTec;'
    cursor = db()
    cursor.fetchall()
    prdct = cursor
    #print(prdct)
    for row in cursor:
        print(row)  # Imprimir cada fila

def dltUsr(id):
    query = "DELETE FROM FichaTec WHERE id_codProduct = ?"
    try:
        cursor = db(query,id)
        #cursor.commit()
        #print("Delete Ok!")
        return "Delete Ok!"
    except SQLAlchemyError as e:
        return "No se pudo eliminar"
    

getAll()
#dltUsr('E-2334')