from src.Controllers.appdb import appDb
import mysql.connector

class appPrindCard():
    def __init__(self):
        self.dtaDb = appDb().connect
        self.cur = self.dtaDb.cursor()

        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

    ############ PROCEDURES TRASACCTIONS ####################
    # INSERT PRINDCARD
    def transctInsertPrindCard(self,*args):
        try:
            self.cursorPool.callproc('InsertPrindCard',(args))
            self.conectPool.commit()
            print("INSERT PRIND OK!")
            #return "INSERT PRIND OK!"
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR PRINDCARD! : ",err )
        finally:
            self.cursorPool.close()

    # UPDATE PRINDCARD
    def transctUpdatePrindCard(self,*args):
        try:
            self.cursorPool.callproc('UpdatePrindCard',(args))
            self.conectPool.commit()
            print(args)
            print("UPDATE PRIND OK!")
            #return "INSERT PRIND OK!"
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR PRINDCARD! : ",err )
        finally:
            self.cursorPool.close()





    #########################################################

    def getPridCardPdf(self,id):
        try:
            query = 'SELECT prindCrdPdf FROM PrindCard WHERE idCodPrdc = %s'
            #cur = self.connect.cursor()
            cur = self.dtaDb.cursor()
            cur.execute(query,(id,))   
            result = cur.fetchone()
            return result
        except:
            print("ERROR AL OBTENER DATOS!")
        finally:
            cur.close()
            self.dtaDb.close()

        


