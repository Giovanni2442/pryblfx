from src.conectDataBase.testConectDb import db

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appImpr():
    def __init__(self):
        self.connect = db()

        # -- METHOD INSERT -- #
    # --- TRANSACCIÓN INSERT --- # 
    def transIsertImprs(self,*args):
        cursor = self.connect.cursor()
        cursor.callproc('InsertImpr',(args))
        self.connect.commit()

            # -- METHOD PUT -- #
    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateImprs(self,*args):
        cursor = self.connect.cursor()
        cursor.callproc('UpdateImpr',(args))
        self.connect.commit()
