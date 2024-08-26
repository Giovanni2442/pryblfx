#from src.conectDataBase.testConectDb import db

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appConvrs():
    def __init__(self):
        #self.connect = db()
        pass

    def postConversion(self,*args):
        #query='''INSERT INTO CONVERSION (idCodPrdc, tipo_Empaque, tipoSello, tipoAcabado, prdctPerf, cntPerf, prdctSuaje, tipSuaje, empcdPrdct, cantPzsPacq, tipEmblj, medidEmblj, pesarProd, pesoProm, etiquetado, tarima_Emplaye, tarima_Flejada)
        #    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        #cursor = #self.connect.cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass

    def postMedidEmpq(self,*args):
        query='''INSERT INTO MedidEmpq(idCodPrdc, ancho, alto)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass

    def postNumBlts_CajsCmas_CmasTarim(self,*args):
        query='''INSERT INTO NumBlts_CajsCmas_CmasTarim(idCodPrdc,cajasCama,camasTarima)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass

    def postNumBlts_CajsTarim(self,*args):
        query='''INSERT INTO NumBlts_CajsTarim(idCodPrdc,num,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass

    def postPsPromTam(self,*args):
        query='''INSERT INTO psPromTam(idCodPrdc,peso,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass