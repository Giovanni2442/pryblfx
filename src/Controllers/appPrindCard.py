from src.Controllers.appdb import appDb
import mysql.connector

class appPrindCard():
    def __init__(self):
        self.dtaDb = appDb().connect
        self.cur = self.dtaDb.cursor()

        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

    ############ PROCEDURES TRASACCTIONS ALMACENAMIENTO EN SQL ####################
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
            self.cursorPool.callproc('UpdatePrindCardUrl_PRU',(args))
            self.conectPool.commit()
            #print(args)
            print("UPDATE PRIND OK!")
            #return "INSERT PRIND OK!"
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR PRINDCARD! : ",err )
        finally:
            self.cursorPool.close()

    #########################################################

    ############ PROCEDURES TRASACCTIONS PRUEBAS ALAMACENAMIENTO EN LOCAL ####################
    # GET OBSERVACIÓNES
    # --- TRANSACCIÓN GET --- #
    def transactGetObsrv(self,id):
        try:
            self.cursorPool.callproc('getObsrv',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            return data
        except mysql.connector.Error as err:
            print("ERROR EN GET OBSRVS",err)
        finally:
            self.cursorPool.close() 
    
    # INSERT PRINDCARD
    def transctInsertPrindCardLOCAL(self,*args):
        try:
            self.cursorPool.callproc('InsertPrindCardUrl_PRU',(args))  
            self.conectPool.commit()
            print("INSERT PRIND OK!")
            #return "INSERT PRIND OK!"
        except mysql.connector.Error as err:
            print("ERROR AL INSERTAR PRINDCARDLOCAL! : ",err )
        finally:
            self.cursorPool.close()

    # UPDATE PRINDCARD
    def transctUpdatePrindCardLOCAL(self,*args):
        try:
            self.cursorPool.callproc('UpdatePrindCardUrl_PRU',(args))
            self.conectPool.commit()
            #print(args)
            print("UPDATE PRIND OK!")
            #return "INSERT PRIND OK!"
        except mysql.connector.Error as err:
            print("ERROR AL ACTUALIZAR PRINDCARDLOCAL! : ",err )
        finally:
            self.cursorPool.close()

    # UPDATE MASIVO DE FICHAS
    def transctUpdateMSVPrindCardLOCAL(self,*args):
        try:
            self.cursorPool.callproc('UpdtMsvFichaVentasID',(args))
            self.conectPool.commit()
            #print(args)
            print("UPDATE PRIND OK!")
            #return "INSERT PRIND OK!"
        except mysql.connector.Error as err:
            print("ERROR AL ACTUALIZAR PRIND CARDLOCAL! : ",err )
        finally:
            self.cursorPool.close()

    # OBTENER LA RUTA DEL PDF
    def getPridCardPdfLOCAL(self,id):
        try:
            query = 'SELECT prindCrdPdf_URL FROM PrindCardLOCAL WHERE idCodPrdc = %s'
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

    # OBTENER LA RUTA DE LAS IMAGENES
    def getPridCardImagesLOCAL(self,id):
        try:
            query = 'SELECT * FROM UrlImgsPdf WHERE idCodPrdc = %s'
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

    
    #########################################################

