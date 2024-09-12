from src.Controllers.appAux import appAux

class appInserts():
    def __init__(self):
        super().__init__()

        # -- CLASE AUXILIAR DE DATOS -- #
        self.aux = appAux()
    
    # RECOLECTOR DE DATOS PARA CADA ENTRADA
    def qryPost(self,tpl):                     # Recorre las listas de Inputs para colocarlas en una lista
        dtaList = self.aux.qryPost(tpl)
        #print("-----------> AQUII: " ,lista)
        #'''
                # --- INSERCIÓN POR REBANADAS ---   

            # --- PRUEBAS FICHA / VENTAS
        self.aux.dataTbl().transactInsrtFichVents(*dtaList[:10])
        
            # --- EXTRUCIÓN ---
        self.aux.dtaExtr().transctInsertExtrs(dtaList[0],*dtaList[10:38])
        
            # --- IMPRESION ---
        self.aux.dtaImpr().transIsertImprs(dtaList[0],*dtaList[38:73])
        
            # --- LAMINACIÓN ---
        self.aux.dtaLam().transctInsertLam(dtaList[0],*dtaList[73:94])
        self.aux.dtaLam().transctInsertLmns(dtaList[0],*dtaList[94:122])

            # --- REFILADO ---
        self.aux.dtaRef().transInsertRefil(dtaList[0],*dtaList[122:150])

            # --- CONVERSION ---
        self.aux.dtaConvrs().transInsertConvrs(dtaList[0],*dtaList[150:174])
        #'''