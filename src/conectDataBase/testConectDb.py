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
    


