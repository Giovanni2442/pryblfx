#from src.conectDataBase.testConectDb import db

# --- QUERY´S LAMINASION  ---
class appLam():
    def __init__(self):
        #self.connect = db()
        # lamina general #
        pass
    def      postLam(self,*args):
        query='''INSERT INTO LAMINADO(idCodPrdc, estructProduct, maxEmpalmesBob, orientBobRack, tipoEmpaqBob, etiquetado, pesarProduct,psoNtoBob)  
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"
        pass
             
    def postMedidManga(self,*args):     # Medida de la manga
        query='''INSERT INTO MedidManga(idCodPrdc,medidaManga,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"
        pass
            
    def postAnchoCore_TolrLam(self,*args):     # Ancho core y Tolerancia
        query='''INSERT INTO AnchoCore_TolrLam(idCodPrdc,anchoCore,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postDiametro_GrosCore(self,*args):     # Ancho core y Tolerancia
        query='''INSERT INTO Diametro_GrosCore(idCodPrdc,diametro,grosorCore)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postDiametro_Bob_Tolr(self,*args):     # Ancho core y Tolerancia
        query='''INSERT INTO Diametro_Bob_Tolr(idCodPrdc,diametroBob,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    ##########################################
        # MATERIAL IMPRESO # 
    def postMaterial_Impreso(self,*args):
        query='''INSERT INTO Material_Impreso(idCodPrdc,mtrlImprs,tipoTratado)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postCalibrePelic_Tolr(self,*args):
        query='''INSERT INTO CalibrePelic_Tolr(idCodPrdc,calibre,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postAnchoBob_TolrMtrlr(self,*args):
        query='''INSERT INTO AnchoBob_TolrMtrl(idCodPrdc,anchoBob,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    # --- LAMINACIÓNES --- #

        # Lam 1 #

    def postMaterial_Laminar_1(self,*args):
        query='''INSERT INTO Material_Laminar_1(idCodPrdc,Material,tipoTratado,tipoLamin)VALUES(%s,%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postCalibrePelic_TolrLam1(self,*args):
        query='''INSERT INTO CalibrePelic_TolrLam1(idCodPrdc,calibre,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postAnchoBob_TolrLam1(self,*args):
        query='''INSERT INTO AnchoBob_TolrLam1(idCodPrdc,anchoBob,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
        # Lam 2 #

    def postMaterial_Laminar_2(self,*args):
        query='''INSERT INTO Material_Laminar_2(idCodPrdc,Material,tipoTratado,tipoLamin)VALUES(%s,%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postCalibrePelic_TolrLam2(self,*args):
        query='''INSERT INTO CalibrePelic_TolrLam2(idCodPrdc,calibre,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postAnchoBob_TolrLam2(self,*args):
        query='''INSERT INTO AnchoBob_TolrLam2(idCodPrdc,anchoBob,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
        # Lam 3 #

    def postMaterial_Laminar_3(self,*args):
        query='''INSERT INTO Material_Laminar_3(idCodPrdc,Material,tipoTratado,tipoLamin)VALUES(%s,%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postCalibrePelic_TolrLam3(self,*args):
        query='''INSERT INTO CalibrePelic_TolrLam3(idCodPrdc,calibre,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postAnchoBob_TolrLam3(self,*args):
        query='''INSERT INTO AnchoBob_TolrLam3(idCodPrdc,anchoBob,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
        # Lam 4 #

    def postMaterial_Laminar_4(self,*args):
        query='''INSERT INTO Material_Laminar_4(idCodPrdc,Material,tipoTratado,tipoLamin)VALUES(%s,%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postCalibrePelic_TolrLam4(self,*args):
        query='''INSERT INTO CalibrePelic_TolrLam4(idCodPrdc,calibre,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!"

        pass
    def postAnchoBob_TolrLam4(self,*args):
        query='''INSERT INTO AnchoBob_TolrLam4(idCodPrdc,anchoBob,tolerancia)VALUES(%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        #cursor.execute(query,args)
        #self.connect.commit()
        #d "Insert Ok!
        pass        