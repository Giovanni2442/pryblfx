from src.conectDataBase.testConectDb import db

class appPrindCard():
    def __init__(self):
        self.connect = db()

    def postPridCardPdf(self,*args):
        query = '''INSERT INTO PrindCard(idCodPrdc,prindCrdPdf)
                    VALUES (%s,%s);'''
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        self.connect.close()
        return "Insert Ok!"
    
    def getPridCardPdf(self,id):
        query = 'SELECT prindCrdPdf FROM PrindCard WHERE idCodPrdc = %s'
        cursor = self.connect.cursor()
        cursor.execute(query,(id,))
        return cursor.fetchone()
        


