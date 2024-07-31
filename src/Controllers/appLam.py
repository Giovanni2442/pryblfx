from src.conectDataBase.testConectDb import db

# --- QUERY´S LAMINASION  ---
class appLam():
    def __init__(self):
        self.connect = db()
        # lamina general #
    def postLam(self,*args):
        query='''INSERT INTO LAMINADO(idCodPrdc, estructProduct, maxEmpalmesBob, orientBobRack, tipoEmpaqBob, etiquetado, pesarProduct,psoNtoBob)  
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
        # MATERIAL IMPRESO # 
    def postMaterial_Impreso(self,*args):
        query='''INSERT INTO Material_Impreso('idCodPrdc','tipoTratado')VALUES(%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    def postCalibrePelic_Tolr(self,*args):
        query='''INSERT INTO CalibrePelic_Tolr('idCodPrdc','calibre','tolerancia')VALUES(%s,%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    def postAnchoBob_TolrMtrlr(self,*args):
        query='''INSERT INTO AnchoBob_TolrMtrl('idCodPrdc','anchoBob','tolerancia')VALUES(%s,%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    def postAnchoBob_TolrMtrlr(self,*args):
        query='''INSERT INTO AnchoBob_TolrMtrl('idCodPrdc','anchoBob','tolerancia')VALUES(%s,%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    