from src.Controllers.appdb import appDb
import mysql.connector

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appImpr():
    def __init__(self):

        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()
    
        # -- METHOD GET -- #
    #'''
    # --- TRANSACCIÓN GET --- #
    def transGetImprs(self,id):
        try:
            self.cursorPool.callproc('getImprs',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            return data
        except mysql.connector.Error as err:
            print("ERROR AL TRAER DATOS IMPRS! : ",err)
        finally:
            self.cursorPool.close()


    
        # -- METHOD INSERT -- #
    # --- TRANSACCIÓN INSERT --- # 
    def transIsertImprs(self,*args):
        try:
            self.cursorPool.callproc('InsertImprs',(args))
            self.conectPool.commit()
            #print("INSERTADO") 
        except:
            print("ERROR AL INSERTAR!")
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")

            # -- METHOD PUT -- #
    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateImprs(self,*args):
        try:
            self.cursorPool.callproc('UpdateImpr',(args))
            self.conectPool.commit()
        except:
            print("ERROR UPDATE")
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")

    ################ UPDATE MASIVO #################
    
    # --- TRANSACCIÓN UPDATE MASIVO --- #
    def transctUpdateMsvImprs(self,*args):
        try:
            self.cursorPool.callproc('UpdtMsvImprs',(args))
            self.conectPool.commit()
            print("ACTUALIZACIÓN IMPRS MASIVA EXITOSA!")
        except mysql.connector.Error as err:
            print("ERROR UPDATE IMPRS MSV : ", err)
        finally:
            self.cursorPool.close()

    # --- TRANSACCIÓN UPDATE POR ID´D SELECCIÓNADOS --- #
    def transctUpdateMsvImprsID(self,*args):
        print(args)
        #'''
        try:
            self.cursorPool.callproc('UpdtMsvImprsID',(args))
            self.conectPool.commit()
            print("ACTUALIZACIÓN MASIVA EN EXTRS EXITOSA!")
        except mysql.connector.Error as err:
            print("ERROR UPDATE EXTRS MSV : ", err)
        finally:
            self.cursorPool.close()#'''

    ################################################
#'''