from src.conectDataBase.testConectDb import db

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appImpr():
    def __init__(self):
        self.connect = db()

    # --- TABLA PADRE IMPRESIÓN ---
    def postImprs(self,*args):
        query='''INSERT INTO IMPRESION (idCodPrdc,material_Imprimir,dinaje,grosor_Core,desarrolloImpr,rep_Eje,rep_Dessr,cant_TintasImpr,tipoImpr,tipoTintas_Utilizar,tipo_Barniz,figEmbob_Impr,maxEmpalmes,tipoEmpaqBob,orientBob_Tarima,pesarProduct, etiquetado,Num_bob_tarima,tarima_Emplaye,tarima_Flejada)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- CalibrePel_Tolr ---
    def postCalibrePel_Tolr(self,*args):
        query = '''INSERT INTO CalibrePel_Tolr(idCodPrdc,calibre,tolerancia)
                 VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"