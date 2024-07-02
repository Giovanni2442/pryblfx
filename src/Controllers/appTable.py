from src.conectDataBase.conectDb import db

class Controllers():
    def __init__(self):
        self.connect = 0

    def get_row_Table(self):
        query = 'SELECT * FROM FichaTec;'
        self.connect = db(query).fetchall()
        return self.connect
    
#pr = Controllers()
#print(pr.get_row_Table())
