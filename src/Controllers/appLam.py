from src.Controllers.appdb import appDb
import mysql.connector

# --- QUERY´S LAMINASION  ---
class appLam():
    def __init__(self):
        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

        # --- METHOD GET --- #
            # ...

        # --- METHOD INSERT --- #

    # --- TRANSACCIÓN INSERT LAMINACIÓN / MATERIAL IMPRESO --- #
    def transctInsertLam(self,*args):
        try:
            self.cursorPool.callproc('InsertLam',(args))
            self.conectPool.commit()
            print("INSERTADO LAM!")
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR LAM",err)
        finally:
            self.cursorPool.close()
            print("Conexión cerrada!")
            
    # --- TRANSACCIÓN INSERT MATERIALES A IMPRIMIR --- #
    def transctInsertLmns(self,*args):
        try:
            self.cursorPool.callproc('InsertLmns',(args))
            self.conectPool.commit()
            print("INSERTADO LAMINASIONES!")
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR LAMINS",err)
        finally:
            self.cursorPool.close()
            print("Conexión cerrada!")


            # --- METHOD UPDATE --- #

                # ...
            
