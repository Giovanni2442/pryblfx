from src.conectDataBase.testConectDb import db

class appFichVent():
    def __init__(self):
        self.connect = db()

    def get(slef):
        pass

    # --- TABLA PADRE EXTRUSIÓN ---
    def postExtr(self,*args):
        query='''INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- CalibrePel_Tolr ---
    def postCalibrePel_Tolr(self,*args):
        query = '''INSERT INTO CalibrePel_Tolr(idCodPrdc,calibre,tolerancia)
                VALUES  (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- AnchoBob_Tolr ---
    def postAnchoBob_Tolr(self,*args):
        query = '''INSERT INTO AnchoBob_Tolr(idCodPrdc,anchoBob,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- AnchoCore_Tolr ---
    def AnchoCore_Tolr(self,*args):
        query='''INSERT INTO AnchoCore_Tolr(idCodPrdc,anchoCore,tolerancia)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- DiametroBob_Tolr ---
    def DiametroBob_Tolr(self,*args):
        query='''INSERT INTO DiametroBob_Tolr(idCodPrdc,diamBob,tolerancia)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Peso_Prom_Bob ---
    def Peso_Prom_Bob(self,*args):
        query='''INSERT INTO Peso_Prom_Bob(idCodPrdc,pesoBob,tolerancia)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Num_BobCama_CamTam ---
    def Num_BobCama_CamTam(self,*args):
        query='''INSERT INTO Num_BobCama_CamTam(idCodPrdc,num_Bob_Cama,camas_Tarima)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Peso_prom_tarima ---
    def Peso_prom_tarima(self,*args):
        query='''INSERT INTO Peso_prom_tarima(idCodPrdc,peso_neto,tolerancia)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"

