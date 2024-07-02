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
    def edit_row_Table(self):
        pass

    # Delete any product select in the row
    def delete_row_Table(self,id):
        query = 'DELETE FROM FichaTec WHERE id_codProduct = %s'
        cursor = self.connect.cursor()
        cursor.execute(query,(id,))
        self.connect.commit()
        return "Delete Ok!"
    
pr = Controllers()
#print(pr.delete_row_Table("E-2335"))
#print(pr.get_row_Table())
