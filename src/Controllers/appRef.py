from src.Controllers.appdb import appDb
import mysql.connector

class appRef():
    def __init__(self) :
        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

    # --- METHOD GET --- #

    # --- TRANSACCIÓN GET --- #
    def transGetRefil(self,id):
        try:
            self.cursorPool.callproc('getRefil',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            return data
        except mysql.connector.Error as err:
            print("ERROR AL TRAER DATOS REFIL! : ",err)
        finally:
            self.cursorPool.close()

    # --- METHOD INSERT --- #

    # --- TRANSACCIÓN INSERT --- # 
    def transInsertRefil(self,*args):
        try:
            self.cursorPool.callproc('InsertRefil',(args))
            self.conectPool.commit()
            print("INSERTADO") 
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR REFIL!",err)
        finally:
            self.cursorPool.close()
            print("Conexión cerrada!")

    # --- METHOD UPDATE --- #

    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateRefil(self,*args):
        try:
            self.cursorPool.callproc('UpdateImpr',(args))
            self.conectPool.commit()
        except mysql.connector.Error as err:
            print("ERROR UPDATE REFIL",err)
        finally:
            self.cursorPool.close()
            print("Conexión cerrada!")    