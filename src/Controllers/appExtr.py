from src.conectDataBase.testConectDb import dbPoll
from src.conectDataBase.testConectDb import db

class appExtr():
    def __init__(self):

        self.connect = db()

        self.connectPool = dbPoll()
        self.conex = self.connectPool.get_connection()
        self.cursor = self.conex.cursor()

        # -- METHOD GET -- #
    def getExtr(self,id):
        query = '''
        SELECT * FROM EXTRUSION extr
	        INNER JOIN CalibrePel_Tolr cltr ON extr.idCodPrdc = cltr.idCodPrdc
            INNER JOIN AnchoBob_TolrExtr anchBob ON extr.idCodPrdc = anchBob.idCodPrdc
            INNER JOIN AnchoCore_TolrExtr anchCor ON extr.idCodPrdc = anchCor.idCodPrdc
            INNER JOIN DiametroBob_Tolr didmBob ON extr.idCodPrdc = didmBob.idCodPrdc
            INNER JOIN Peso_Prom_Bob psPrmBob ON extr.idCodPrdc = psPrmBob.idCodPrdc
            INNER JOIN Num_BobCama_CamTam numBobCam ON extr.idCodPrdc = numBobCam.idCodPrdc
            INNER JOIN Peso_prom_tarimaExtr psPrmTrm ON extr.idCodPrdc = psPrmTrm.idCodPrdc
        WHERE extr.idCodPrdc = %s;'''
        cursor = self.connect.cursor()
        cursor.execute(query,(id,))
        result = cursor.fetchall()
        return result
    
        # -- METHOD GET -- #
    # --- TRANSACCIÓN GET --- #
    def transactGetExtrs(self,id):
        self.cursor.callproc('getExtrs',[id])
        
        # Recuperar los resultados
        for result in self.cursor.stored_results():
            data = result.fetchall()

        self.cursor.close()
        self.conex.close()
        return data
    
    # --- TRANSACCIÓN INSERT --- #
    def transctInsertExtrs(self,*args):
        self.cursor.callproc('InsertExtr',(args))
        self.conex.commit()

        # -- METHOD PUT -- #
    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateExtrs(self,*args):
        self.cursor.callproc('UpdateEtrs',(args))
        self.conex.commit()


