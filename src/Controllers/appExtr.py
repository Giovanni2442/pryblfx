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
        
        # -- METHOD POST -- #
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
                 VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- AnchoBob_Tolr ---
    def postAnchoBob_Tolr(self,*args):
        query = '''INSERT INTO AnchoBob_TolrExtr(idCodPrdc,anchoBob,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
   # --- AnchoCore_Tolr ---
    def postAnchoCore_Tolr(self,*args):
        query = '''INSERT INTO AnchoCore_TolrExtr(idCodPrdc,anchoCore,tolerancia)
                VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    # --- DiametroBob_Tolr ---
    def postDiametroBob_Tolr(self,*args):
        query = '''INSERT INTO DiametroBob_Tolr(idCodPrdc,diamBob,tolerancia)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Peso_Prom_Bob ---
    def postPeso_Prom_Bob(self,*args):
        query = '''INSERT INTO Peso_Prom_Bob(idCodPrdc,pesoBob,tolerancia)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Num_BobCama_CamTam ---
    def postNum_BobCama_CamTam(self,*args):
        query = '''INSERT INTO Num_BobCama_CamTam(idCodPrdc,num_Bob_Cama,camas_Tarima)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Peso_prom_tarima ---
    def postPeso_prom_tarima(self,*args):
        query = '''INSERT INTO Peso_prom_tarimaExtr(idCodPrdc,peso_neto,tolerancia)
            VALUES (%s,%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
        # -- METHOD PUT -- #

    def putExtr(self,*args):
        query='''
            UPDATE EXTRUSION
            SET tipo_Material = %s,
                dinaje = %s,
                formula = %s,
                pigmento_Pelicula = %s,
                tipo_Bobina = %s,
                tipo_Tratado = '%s,
                max_Emplm = %s,
                orient_Bob_Tarima = %s,
                Tipo_Empq_Bob = %s,
                pesar_Prdct = %s,
                etiquetado = %s,
                num_Bob_Tarima = %s,
                tarima_Emplaye = %s,
                tarima_flejada = %s,
                numBobTam = %s
            WHERE idCodPrdc = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Update Ok!"
    
     # --- CalibrePel_Tolr ---
    def putCalibrePel_Tolr(self,*args):
        query = '''
            UPDATE CalibrePel_Tolr
            SET calibre = %s,
                tolerancia = %s
            WHERE idCodPrdc = %s
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Update Ok!"
    
     # --- AnchoBob_Tolr ---
    def putAnchoBob_Tolr(self,*args):
        query = '''
            UPDATE AnchoBob_TolrExtr
            SET anchoBob = %s,
                tolerancia = %s
            WHERE idCodPrdc = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
   # --- AnchoCore_Tolr ---
    def putAnchoCore_Tolr(self,*args):
        query = '''
            UPDATE AnchoCore_TolrExtr
            SET anchoCore = %s,
                tolerancia = %s
            WHERE idCodPrdc = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
    # --- DiametroBob_Tolr ---
    def putDiametroBob_Tolr(self,*args):
        query = '''
            UPDATE DiametroBob_Tolr
            SET diamBob = %s,
                tolerancia = %s
            WHERE idCodPrdc = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Peso_Prom_Bob ---
    def putPeso_Prom_Bob(self,*args):
        query = '''
            UPDATE Peso_Prom_Bob
            SET pesoBob = %s,
                tolerancia = %s
            WHERE idCodPrdc = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Num_BobCama_CamTam ---
    def putNum_BobCama_CamTam(self,*args):
        query = '''
            UPDATE Num_BobCama_CamTam
            SET num_Bob_Cama = %s,
                camas_Tarima = %s
            WHERE idCodPrdc = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- Peso_prom_tarima ---
    def putPeso_prom_tarima(self,*args):
        query = '''
            UPDATE Peso_prom_tarimaExtr
            SET peso_neto = %s,
                tolerancia = %s
            WHERE idCodPrdc = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
