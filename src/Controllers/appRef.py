#from src.conectDataBase.testConectDb import db

class appRef():
    def __init__(self) :
        #self.connect = db()     #conect to data base
        pass

    def postRefilado(self,*args):
        query='''INSERT INTO REFILADO (idCodPrdc, proceso, acabadoBob, grosorCore, figEmbob_impr, bobinaRefilar, maximo_Empal, señalEmpl, orient_Bob_Tarima, tipo_Empaque, pesar_Prdct, etiquetado, tarima_emplaye, tarima_flejada, numBobTam)
            VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass
    
    def postAnchoFinalBob_TolrRef(self,*args):
        query='''INSERT INTO AnchoFinalBob_TolrRef (idCodPrdc,anchoFinalBob,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass
    def postMetrosBobRefil_Tolr(self,*args):
        query='''INSERT INTO MetrosBobRefil_Tolr (idCodPrdc,metros,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass
    def postDiamBobRefil_Tolr(self,*args):
        query='''INSERT INTO DiamBobRefil_Tolr (idCodPrdc,diametro,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass
    def postPesoNet_Prom_Bob(self,*args):
        query='''INSERT INTO PesoNet_Prom_Bob (idCodPrdc,peso,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass
    def postNum_BobCama_CamTamRefil(self,*args):
        query='''INSERT INTO Num_BobCama_CamTamRefil (idCodPrdc,num_Bob_Cama,camas_Tarima)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass
    def postPeso_prom_tarimaRefil(self,*args):
        query='''INSERT INTO Peso_prom_tarimaRefil (idCodPrdc,pesoNeto,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!"
        pass
    def postAnchCre_Tol(self,*args):
        query='''INSERT INTO anchCre_TolRefil(idCodPrdc,core,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #return "Insert Ok!"
        pass
    def postNumBobTam(self,*args):
        query='''INSERT INTO numBobTam(idCodPrdc,core,tolerancia)
            VALUES (%s,%s,%s)'''
        #cursor = #self.connect.#cursor()
        ##cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        #cursor.execute(query,args)
        #self.connect.commit()
        #return "Insert Ok!" 
        pass