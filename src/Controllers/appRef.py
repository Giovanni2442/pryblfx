from src.Controllers.appdb import appDb
import mysql.connector

class appRef():
    def __init__(self) :
        self.dtaPool = appDb().conexPool
        self.conectPool = self.dtaPool.get_connection()
        self.cursorPool =  self.conectPool.cursor()

    # --- METHOD GET --- #

    # --- TRANSACCIÓN GET --- #
    def transGetImprs(self,id):
        try:
            self.cursorPool.callproc('getImprs',[id])
            # Recuperar los resultados
            for result in self.cursorPool.stored_results():
                data = result.fetchone()
            return data
        except mysql.connector.Error as err:
            print("ERROR AL TRAER DATOS IMPRS! : ",err)
        finally:
            self.cursorPool.close()

    # --- METHOD INSERT --- #

    # --- TRANSACCIÓN INSERT --- # 
    def transIsertImprs(self,*args):
        try:
            self.cursorPool.callproc('InsertImprs',(args))
            self.conectPool.commit()
            print("INSERTADO") 
        except:
            print("ERROR AL INSERTAR!")
        finally:
            self.cursorPool.close()
            print("Conexión cerrada!")

    # --- METHOD UPDATE --- #

    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateImprs(self,*args):
        try:
            self.cursorPool.callproc('UpdateImpr',(args))
            self.conectPool.commit()
        except:
            print("ERROR UPDATE")
        finally:
            self.cursorPool.close()
            print("Conexión cerrada!")    


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