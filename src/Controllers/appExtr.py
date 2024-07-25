from src.conectDataBase.testConectDb import db

class appFichVent():
    def __init__(self):
        self.connect = db()

    def get(slef):
        pass

    def post_data(self,*args):
        # INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2335','Fresno','granos','03/07/2024','SS');
        query = 'INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES (%s,%s,%s,%s,%s);'
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!" 