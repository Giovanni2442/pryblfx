from src.conectDataBase.testConectDb import dbPoll

# --- QUERY´S IMPRESIÓN DIGITAL ---
class appImpr():
    def __init__(self):
        
        self.connectPool = dbPoll()
        self.conex = self.connectPool.get_connection()
        self.cursor = self.conex.cursor()

        # -- METHOD INSERT -- #
    # --- TRANSACCIÓN INSERT --- # 
    def transIsertImprs(self,*args):
        self.cursor.callproc('InsertImprs',(args))
        self.conex.commit()

            # -- METHOD PUT -- #
    # --- TRANSACCIÓN UPDATE --- #
    def transctUpdateImprs(self,*args):
        self.cursor.callproc('UpdateImpr',(args))
        self.conex.commit()

