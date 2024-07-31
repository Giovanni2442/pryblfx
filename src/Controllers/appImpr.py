from src.conectDataBase.testConectDb import db

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appImpr():
    def __init__(self):
        self.connect = db()

    # --- TABLA PADRE IMPRESIÓN ---
    def postImprs(self,*args):
        query='''INSERT INTO IMPRESION (idCodPrdc,material_Imprimir,dinaje,grosor_Core,desarrolloImpr,rep_Eje,rep_Dessr,cant_TintasImpr,tipoImpr,tipoTintas_Utilizar,tipo_Barniz,figEmbob_Impr,maxEmpalmes,tipoEmpaqBob,orientBob_Tarima,pesarProduct, etiquetado,Num_bob_tarima,tarima_Emplaye,tarima_Flejada)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Validación de color ---
    def postVldClr(self,*args):
        query = '''INSERT INTO vldClr(idCodPrdc,color,tolDelts)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    # --- Calibre del material y tolerancia ---
    def postCalMater_Tolr(self,*args):
        query = '''INSERT INTO CalMater_Tolr(idCodPrdc,calibre,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    # --- Ancho de bobina a imprimir y tolerancia ---
    def postAnchoBobImpr_Tolr(self,*args):
        query = '''INSERT INTO AnchoBobImpr_Tolr(idCodPrdc,ancho,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Ancho de core y tolerancia ---
    def postAnchoCore_TolrImpr(self,*args):
        query = '''INSERT INTO AnchoCore_TolrImpr(idCodPrdc,ancho_Core,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
      # --- Diametro de bobina y Tolerancia ---
    def postAnchoDiamBob_Tolr(self,*args):
        query = '''INSERT INTO DiamBob_Tolr(idCodPrdc,diametro,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    
      # --- Ancho de core y tolerancia ---
    def postPesoPromBob(self,*args):
        query = '''INSERT INTO PesoPromBob(idCodPrdc,peso,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
      # --- Numero de bobinas por cama y camas por tarima ---
    def postNum_BobCama_CamaTarima(self,*args):
        query = '''INSERT INTO Num_BobCama_CamaTarima(idCodPrdc,numBobCama,camaTam)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
      # --- Peso neto promedio por tarima y tolerancia ---
    def postPeso_prom_tarimaImpr(self,*args):
        query = '''INSERT INTO Peso_prom_tarimaImpr(idCodPrdc,pesoNto,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"