from src.Controllers.appdb import appDb
import mysql.connector

class appSec():
  def __init__(self):
    self.dtaPool = appDb().conexPool
    self.conectPool = self.dtaPool.get_connection()
    self.cursorPool =  self.conectPool.cursor()
    
  # ---- METHOD GET --- #
  def transGetProceso(self,id):
    try:
      self.cursorPool.callproc('getSecpdf',[id])
      # Recuperar los resultados
      for result in self.cursorPool.stored_results():
          data = result.fetchone()
      return data
    except mysql.connector.Error as err:
      print("ERROR AL TRAER DATOS PROCESOS! : ",err)
    finally:
      self.cursorPool.close()

  def transInsertProceso(self,*args):
      try:
        self.cursorPool.callproc('InsertSecPdf',(args))
        self.conectPool.commit()
        #print("PROCESO INSERTADO!")
        return "PROCESO INSERTADO!"
      except mysql.connector.Error as err:
        #print("ERROR AL INSERTAR PROCESO!",err)
        return "ERROR AL INSERTAR PROCESO!",err
      finally:
          self.cursorPool.close()
          #print("Conexión cerrada!")

  def transUpdateProceso(self,*args):
    try:
      self.cursorPool.callproc('UpdateSecPdf',(args))
      self.conectPool.commit()
    except mysql.connector.Error as err:
        print("ERROR UPDATE PROCESO",err)
    finally:
        self.cursorPool.close()
        #print("Conexión cerrada!")    
    