from src.conectDataBase.testConectDb import db

class appFichVent():
    def __init__(self):
        self.connect = db()

    def get(slef):
        pass

    # --- TABLA PADRE EXTRUSIÓN ---
    def postExtr(self,*args):
        query='''INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada)
            VALUES ('E-2334','rr','rr','rr','rr','rr','qe',10,'qe','qe','qe','qe',88,'qe','qe');'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- CalibrePel_Tolr ---
    def postCalibrePel_Tolr(self,*args):
        query = '''INSERT INTO CalibrePel_Tolr(idCodPrdc,calibre,tolerancia)
                VALUES  ('E-2335',30,40);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- AnchoBob_Tolr ---
    def postAnchoBob_Tolr(self,*args):
        query = '''INSERT INTO AnchoBob_Tolr(idCodPrdc,anchoBob,tolerancia)
                VALUES ('E-2334',30,40);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- TABLA PADRE EXTRUSIÓN ---
    def postExtr(self,*args):
        query='''INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada)
            VALUES ('E-2334','rr','rr','rr','rr','rr','qe',10,'qe','qe','qe','qe',88,'qe','qe');'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- TABLA PADRE EXTRUSIÓN ---
    def postExtr(self,*args):
        query='''INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada)
            VALUES ('E-2334','rr','rr','rr','rr','rr','qe',10,'qe','qe','qe','qe',88,'qe','qe');'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- TABLA PADRE EXTRUSIÓN ---
    def postExtr(self,*args):
        query='''INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada)
            VALUES ('E-2334','rr','rr','rr','rr','rr','qe',10,'qe','qe','qe','qe',88,'qe','qe');'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    
     # --- TABLA PADRE EXTRUSIÓN ---
    def postExtr(self,*args):
        query='''INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada)
            VALUES ('E-2334','rr','rr','rr','rr','rr','qe',10,'qe','qe','qe','qe',88,'qe','qe');'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
