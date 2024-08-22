from src.conectDataBase.testConectDb import db

class appExtr():
    def __init__(self):
        self.connect = db()

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
    
        # -- METHOD INSERT -- #
    # --- TRANSACCIÓN INSERT --- #
    def transctInsertExtrs(self,*args):
        cursor = self.connect.cursor()
        cursor.callproc('InsertExtr',(args))
        self.connect.commit()
    
        # -- METHOD PUT -- #
    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateExtrs(self,*args):
        cursor = self.connect.cursor()
        cursor.callproc('UpdateExtr',(args))
        self.connect.commit()
