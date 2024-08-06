from src.conectDataBase.testConectDb import db


# QUERY PARA ALMACENAR LOS PDF
class appPrindPdf():
    def __init__(self):
        self.connect = db()
        # lamina general #
    def postPdf(self,*args):
        query='''INSERT INTO PrindCard(idCodPrdc,prindCrdPdf)  
        VALUES (%s,%s);'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
