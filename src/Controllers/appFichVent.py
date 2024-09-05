#'''

from src.Controllers.appdb import appDb
import mysql.connector #'''

class appFichVent():
    def __init__(self):
        #pass
        #'''
        self.dtaDb = appDb().connect
        self.cur = self.dtaDb.cursor()

        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

            # --- FICHA TECNICA TABLA PADRE ----
  
    # --- METHOD GET ----
    # Show all products
    #'''
    #@classmethod


    ## -- ACTUALIZACIÓNES MASIVAS -- ##

    def get_row_clientes(self):
        try:
            query = 'SELECT DISTINCT cliente FROM FichaTec;'
            #cur = self.connect.cursor()
            cur = self.dtaDb.cursor()
            cur.execute(query)   
            result = cur.fetchall()
            return result
        except:
            print("ERROR AL OBTENER DATOS!")
        finally:
            cur.close()
            self.dtaDb.close()

    ###################################


    def get_row_Table(self):
        try:
            query = 'SELECT * FROM FichaTec;'
            #cur = self.connect.cursor()
            cur = self.dtaDb.cursor()
            cur.execute(query)   
            result = cur.fetchall()
            return result
        except:
            print("ERROR AL OBTENER DATOS!")
        finally:
            cur.close()
            self.dtaDb.close()
            #self.connect.close()'''
            
    #'''
    # SHOW WITH ID
    def getFicha(self,id):
        try: 
            query = 'SELECT * FROM FichaTec WHERE id_codProduct = %s;'
            self.cur.execute(query,(id,))
            result = self.cur.fetchone()
            return result
        except:
            print("ERROR AL OBTENER DATOS EN FICHA!")
        finally:
            self.cur.close()
            self.dtaDb.close()
    # ----------------------------'''

    #'''
    # --- METHOD DELETE ----
    # Delete any product select in the row
    def delete_row_Table(self,id):
        try:
            query = 'DELETE FROM FichaTec WHERE id_codProduct = %s'
            self.cur.execute(query,(id,))
            self.dtaDb.commit()
            return "Delete Ok!"
        except mysql.connector.Error as err:
            print("ERROR AL ELIMINAR! : ",err )
        finally:
            self.cur.close()
            self.dtaDb.close()
            '''
    # ----------------------
    
        # --- TABLA VENTAS ---
    '''
    # --- METHOD GET -------
     # SHOW WITH ID
    def get_Ventas(self, id):
        try:
            query = 'SELECT * FROM VENTAS WHERE idCodPrdc = %s;'
            #cur = self.data
            self.cur.execute(query, (id,))
            result = self.cur.fetchone()
            return result
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos o al ejecutar la consulta:", err)
        finally:
            self.cur.close()
            # Cerrar la conexión si no necesitas más consultas
            self.dtaDb.close()
        
    # ----------------------'''

    #### QUERY´S DE PRUEBA ####
    #'''
    def transactInsrtFichVents(self,*args):
        try:
            self.cursorPool.callproc('InsertFichaVentas',(args))
            self.conectPool.commit()
            #print("INSERTADO!")
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR EN FICHA!",err)
        finally:
            self.cursorPool.close()
            #self.conectPool.close()#'''

    #'''
    def transactUpdateFichaVents(self,*args):
            try:
                self.cursorPool.callproc('UpdateFichaVentas',(args))
                self.conectPool.commit()
            except mysql.connector.Error as err:
                print("ERROR GET FICHA",err)
            finally:
                self.cursorPool.close()#'''

    ###################################
    
#pr = Controllers()
#print(pr.delete_row_Table("E-2335"))
#print(pr.get_row_Table())
