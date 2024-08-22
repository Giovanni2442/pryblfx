import os
from dotenv import load_dotenv
import mysql.connector

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
        print("Error: Una o más variables de entorno no están configuradas correctamente.")
        return None

    # Conectar a la base de datos
    try:
        connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=db_name
        )
        #print("Conexión exitosa:", connection)
        return connection
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos:", err)
        return None
    
def dbPoll():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    dbConfig = {
        # Datos para la bd obtenidos de las variables de entorno
        'user' : os.getenv('DB_USER'),
        'password' : os.getenv('DB_PASSWORD'),
        'host' : os.getenv('DB_HOST'),
        'port' : os.getenv('DB_PORT'),
        'database': os.getenv('DB_NAME')
    }

    # Conectar a la base de datos
    try:
        conexPool = mysql.connector.pooling.MySQLConnectionPool(
            pollName = "poolUpdate",
            pool_size=10,
            **dbConfig
        )
        #print("Conexión exitosa:", connection)
        return conexPool
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos:", err)
        return None
    
def dbPoll():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    dbConfig = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_NAME')  # MySQL usa 'database', no 'db_name'
    }

    # Conectar a la base de datos
    try:
        conexPool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="poolUpdate",  # Corregir el nombre del parámetro
            pool_size=5,
            **dbConfig
        )
        #print("Conexión exitosa al pool")
        return conexPool
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos:", err)
        return None


'''
# Ejemplo de uso
pool = dbPoll()

if pool:
    try:
        connection = pool.get_connection()
        print("Conexión obtenida del pool")
        # Aquí puedes trabajar con la conexión obtenida
        connection.close()  # Devuelve la conexión al pool
    except mysql.connector.Error as err:
        print("Error al obtener la conexión del pool:", err)
else:
    print("No se pudo crear el pool de conexiones")
'''


