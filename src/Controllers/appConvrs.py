from src.Controllers.appdb import appDb
import mysql.connector

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appConvrs():
    def __init__(self):
        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

    # --- TRANSACCIÓN GET --- #
    def transGetConvrs(self,id):
        try:
            self.cursorPool.callproc('getConvrs',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            #print("-- : ",data)
            return data
        except mysql.connector.Error as err:
            print("ERROR AL TRAER DATOS CONVRS! : ",err)
        finally:
            self.cursorPool.close()

    # --- METHOD INSERT --- #

    # --- TRANSACCIÓN INSERT --- # 
    def transInsertConvrs(self,*args):
        try:
            self.cursorPool.callproc('InsertConvrs',(args))
            self.conectPool.commit()
            #print("INSERTADO") 
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR CONVRS!",err)
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")

    # --- METHOD UPDATE --- #

    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateConvrs(self,*args):
        try:
            self.cursorPool.callproc('UpdateConvrs',(args))
            self.conectPool.commit()
        except mysql.connector.Error as err:
            print("ERROR UPDATE CONVRS",err)
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")  
    