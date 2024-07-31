from src.conectDataBase.testConectDb import db

# --- QUERY´S LAMINASION  ---
class appLam():
    def __init__(self):
        self.connect = db()

    def postLam(self,*args):
        query='''INSERT INTO LAMINADO(idCodPrdc, estructProduct, tipoTratado, maxEmpalmesBob, orientBobRack, tipoEmpaqBob, etiquetado, pesarProduct) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,);'''
        cursor = self.connect.cursor()
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"