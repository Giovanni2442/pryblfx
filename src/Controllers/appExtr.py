from src.Controllers.appdb import appDb
import mysql.connector

class appExtr():
    def __init__(self):
        
        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()
        
        # -- METHOD GET -- #    
    #'''
    # --- TRANSACCIÓN GET --- #
    def transactGetExtrs(self,id):
        try:
            self.cursorPool.callproc('getExtrs',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            return data
        except mysql.connector.Error as err:
            print("ERROR EN GET EXTR",err)
        finally:
            self.cursorPool.close() 
    
    # --- TRANSACCIÓN INSERT --- #
    def transctInsertExtrs(self,*args):
        try:
            self.cursorPool.callproc('InsertExtr',(args))
            self.conectPool.commit()
            #print("INSERTADO")
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR EXTRS",err)
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")

        # -- METHOD PUT -- #
    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateExtrs(self,*args):
        try:
            self.cursorPool.callproc('UpdateEtrs',(args))
            self.conectPool.commit()
            print("ACTUALIZADO")
        except mysql.connector.Error as err:
            print("ERROR UPDATE EXTRS : ", err)
        finally:
            self.cursorPool.close()#'''
            
    ################ UPDATE MASIVO #################
    
    # --- TRANSACCIÓN UPDATE MASIVO --- #
    def transctUpdateMsvExtrs(self,*args):
        try:
            self.cursorPool.callproc('UpdtMsvExtrs',(args))
            self.conectPool.commit()
            print("ACTUALIZACIÓN MASIVA EXITOSA!")
        except mysql.connector.Error as err:
            print("ERROR UPDATE EXTRS MSV : ", err)
        finally:
            self.cursorPool.close()



    ################################################

