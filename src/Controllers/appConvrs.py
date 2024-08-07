from src.conectDataBase.testConectDb import db

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appConvrs():
    def __init__(self):
        self.connect = db()

    def postConversion(self,*args):
        query='''INSERT INTO CONVERSION (idCodPrdc, tipo_Empaque, tipoSello, tipoAcabado, perf, llevaSuaj, suaje, empcProd, cantPzsPacq, embalaje, medidEmblj, pesarProd, pesoProm, etiquetado, tarima_Emplaye, tarima_Flejada)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    def postMedidEmpq(self,*args):
        query='''INSERT INTO MedidEmpq(idCodPrdc, ancho, alto)
            VALUES (%s,%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    def postNumBlts_CajsCmas_CmasTarim(self,*args):
        query='''INSERT INTO NumBlts_CajsCmas_CmasTarim(idCodPrdc,cajasCama,camasTarima)
            VALUES (%s,%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    def postNumBlts_CajsTarim(self,*args):
        query='''INSERT INTO NumBlts_CajsTarim(idCodPrdc,peso,tolerancia)
            VALUES (%s,%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    def postPsPromTam(self,*args):
        query='''INSERT INTO psPromTam(idCodPrdc,peso,tolerancia)
            VALUES (%s,%s,%s)'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"