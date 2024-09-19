from src.Controllers.appdb import appDb
import mysql.connector

# --- QUERY´S LAMINASION  ---
class appLam():
    def __init__(self):
        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

    # --- METHOD GET --- #

    # --- TRANSACCIÓN GET LAMINACIÓN / MATERIAL IMPRESO --- #    
    def transctGetLamGen(self,id):
        try:
            self.cursorPool.callproc('getLamGen',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            return data
        except mysql.connector.Error as err:
            print("ERROR AL TRAER DATOS IMPRS! : ",err)
        finally:
            self.cursorPool.close()
  
    # --- TRANSACCIÓN GET MATERIALES A IMPRIMIR --- #    
    def transctGetLmns(self,id):
        try:
            self.cursorPool.callproc('getLmns',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            return data
        except mysql.connector.Error as err:
            print("ERROR AL TRAER DATOS IMPRS! : ",err)
        finally:
            self.cursorPool.close()

    # --- METHOD INSERT --- #

    # --- TRANSACCIÓN INSERT LAMINACIÓN / MATERIAL IMPRESO --- #
    def transctInsertLam(self,*args):
        try:
            self.cursorPool.callproc('InsertLam',(args))
            self.conectPool.commit()
            #print("INSERTADO LAM!")
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR LAM",err)
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")
            
    # --- TRANSACCIÓN INSERT MATERIALES A IMPRIMIR --- #
    def transctInsertLmns(self,*args):
        try:
            self.cursorPool.callproc('InsertLmns',(args))
            self.conectPool.commit()
            #print("INSERTADO LAMINASIONES!")
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR LAMINS",err)
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")

    # --- METHOD UPDATE --- #
    
    # --- TRANSACCIÓN UPDATE LAMINACIÓN / MATERIAL IMPRESO --- #
    def transctUpdateLamGen(self,*args):
        try:
            self.cursorPool.callproc('UpdateLam',(args))
            self.conectPool.commit()
            #print("ACTUALIZADA LAMINASIO GENERAL!")
        except mysql.connector.Error as err:
            print("ERROR AL ACTUALIZAR LAMGEN",err)
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")

    # --- TRANSACCIÓN UPDATE MATERIALES A IMPRIMIR --- #
    def transctUpdateLmns(self,*args):
        try:
            self.cursorPool.callproc('UpdateLmns',(args))
            self.conectPool.commit()
            #print("ACTUALIZADA LAMINASIO GENERAL!")
        except mysql.connector.Error as err:
            print("ERROR AL ACTUALIZAR LAMINS",err)
        finally:
            self.cursorPool.close()
            #print("Conexión cerrada!")
    

    #################################################################
    '''
            # --- TRANSACCIÓN UPDATE MASIVO --- #
    # -- LAMINACIÓN GENERAL --#
    def transctUpdateMsvLamGeneral(self,*args):
        try:
            self.cursorPool.callproc('UpdtMsvLamGen',(args))
            self.conectPool.commit()
            print("ACTUALIZACIÓN LAM GEN MASIVA EXITOSA!")
        except mysql.connector.Error as err:
            print("ERROR UPDATE LAM GEN MSV : ", err)
        finally:
            self.cursorPool.close()

    # -- LAMINACIÓNES --#
    def transctUpdateMsvLaminas(self,*args):
        try:
            self.cursorPool.callproc('UpdtMsvLaminas',(args))
            self.conectPool.commit()
            print("ACTUALIZACIÓN LAMINAS MASIVA EXITOSA!")
        except mysql.connector.Error as err:
            print("ERROR UPDATE LAMINAS MSV : ", err)
        finally:
            self.cursorPool.close()
        '''

    # ------- MODIFICACIÓNES MASIVAS POR ID´S -----------

    # -- LAMINACIÓN GENERAL --#
    def transctUpdateMsvLamGeneralID(self,*args):
        try:
            self.cursorPool.callproc('UpdtMsvLamGenID',(args))
            self.conectPool.commit()
            #print("ACTUALIZACIÓN LAM GEN MASIVA EXITOSA!")
        except mysql.connector.Error as err:
            print("ERROR UPDATE LAM GEN MSV ID: ", err)
        finally:
            self.cursorPool.close()

    # -- LAMINACIÓNES --#
    def transctUpdateMsvLaminasID(self,*args):
        try:
            self.cursorPool.callproc('UpdtMsvLaminasID',(args))
            self.conectPool.commit()
            #print("ACTUALIZACIÓN LAMINAS MASIVA EXITOSA!")
        except mysql.connector.Error as err:
            print("ERROR UPDATE LAMINAS MSV ID: ", err)
        finally:
            self.cursorPool.close()

    #########################################################################################################         
