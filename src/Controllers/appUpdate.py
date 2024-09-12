from src.Controllers.appAux import appAux

class appUpdate():
    def __init__(self):
        # -- CLASE AUXILIAR DE DATOS -- #
        self.aux = appAux()
    
        # RECOLECTOR DE DATOS PARA CADA ENTRADA
    def qryUpdate(self,tpl):                     # Recorre las listas de Inputs para colocarlas en una lista
        dtaList = self.aux.qryPost(tpl)

        #'''
            #--UPDATE--#
        # --- FICHA / VENTAS ---
        self.aux.dataTbl().transactUpdateFichaVents(*dtaList[1:10],dtaList[0])
        # --- EXTRUSION ---
        self.aux.dtaExtr().transctUpdateExtrs(*dtaList[10:38], dtaList[0]) 
        # --- IMPRESION ---
        self.aux.dtaImpr().transctUpdateImprs(*dtaList[38:73], dtaList[0])#'''
        # --- LAMINACIÓN ---
            # -- LAMIANDO --
        self.aux.dtaLam().transctUpdateLamGen(*dtaList[73:94], dtaList[0])
            # -- MATERIAL LAMINADO --
        self.aux.dtaLam().transctUpdateLmns(*dtaList[94:122],dtaList[0])

        # --- REFILADO ---
        self.aux.dtaRef().transctUpdateRefil(*dtaList[122:150], dtaList[0])
        
        # --- CONVERSION ---
        self.aux.dtaConvrs().transctUpdateConvrs(*dtaList[150:174],dtaList[0])