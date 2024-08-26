#from src.Controllers.appFichVent import appFichVent
from src.conectDataBase.testConectDb import db
from src.conectDataBase.testConectDb import dbpool

    # -- INTERFACE --
# prueba conexión a la base de datos 
class appDb():
    def __init__(self):
        # CONEXIÓN A LA BASE DE DATOS
        self.connect = db()

        # CONEXIÓN AL POOL DE CONSULTAS
        self.conexPool = dbpool()
        #self.dtaFichVen = appFichVent()  #Accede a la información en la base de datos
        #pass