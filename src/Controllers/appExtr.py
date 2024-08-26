from src.Controllers.appdb import appDb

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
        except:
            print("ERROR AL INSERTAR")
        finally:
            self.cursorPool.close() 
    
    # --- TRANSACCIÓN INSERT --- #
    def transctInsertExtrs(self,*args):
        try:
            self.cursorPool.callproc('InsertExtr',(args))
            self.conectPool.commit()
            print("INSERTADO")
        except:
            print("ERROR AL INSERTAR")
        finally:
            self.cursorPool.close()
            print("Conexión cerrada!")

        # -- METHOD PUT -- #
    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateExtrs(self,*args):
        try:
            self.cursorPool.callproc('UpdateEtrs',(args))
            self.conectPool.commit()
            print("ACTUALIZADO")
        except:
            print("ERROR UPDATE")
        finally:
            self.cursorPool.close()#'''
            


