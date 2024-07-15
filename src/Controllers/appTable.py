from src.conectDataBase.testConectDb import db

class Controllers():
    def __init__(self):
        self.connect = db()

    # Show all products
    def get_row_Table(self):
        query = 'SELECT * FROM FichaTec;'
        cursor = self.connect.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
        
    # edit any product select in the row
    def put_row_Table(self):
        pass

    # Delete any product select in the row
    def delete_row_Table(self,id):
        query = 'DELETE FROM FichaTec WHERE id_codProduct = %s'
        cursor = self.connect.cursor()
        cursor.execute(query,(id,))
        self.connect.commit()
        return "Delete Ok!"
    
    # Test Insert in table FichaTecnica 
    def post_data(self,id,cln,fch1,fch2,prdct):
        # INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2335','Fresno','granos','03/07/2024','SS');
        query = 'INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES (%s,%s,%s,%s,%s);'
        cursor = self.connect.cursor()
        cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        self.connect.commit()
        return "Insert Ok!"
    
pr = Controllers()
#print(pr.delete_row_Table("E-2335"))
#print(pr.get_row_Table())