from src.Controllers.appAux import appAux

class appUpdateMasivo():
    def __init__(self):
        # -- CLASE AUXILIAR DE DATOS -- #
        self.aux = appAux()
       
      
        # RECOLECTOR DE DATOS PARA CADA ENTRADA
    #def qryUpdateMsv(self,tpl,cliente):                     # Recorre las listas de Inputs para colocarlas en una lista
    def qryUpdateMsv(self,tpl,ids):
        dtaList = self.aux.qryPost(tpl)
        #'''
          # --- FICHA ---

            #--UPDATE MASSIVE--#
        # --- FICHA / VENTAS ---
        self.dataTbl().transactUpdateFichaVents(*self.auxList[1:10],ids)
        #self.dataTbl().transactUpdateFichaVents(*self.auxList[1:10],self.auxList[0])
        # --- EXTRUSION ---
        self.aux.dtaExtr().transctUpdateMsvExtrsID(*dtaList[10:38],ids) 
        #self.aux.dtaExtr().transctUpdateMsvExtrs(*dtaList[10:38],cliente) 
        
        # --- IMPRESION ---
        #self.aux.dtaImpr().transctUpdateMsvImprs(*dtaList[38:73],cliente)
        self.aux.dtaImpr().transctUpdateMsvImprsID(*dtaList[38:73],ids)

        # --- LAMINACIÓN ---
            # --- GENERAL --
        self.aux.dtaLam().transctUpdateMsvLamGeneralID(*dtaList[73:94], ids)
        #self.aux.dtaLam().transctUpdateMsvLamGeneral(*dtaList[73:94], cliente)
        
            # -- MATERIAL LAMINADO --
        self.aux.dtaLam().transctUpdateMsvLaminasID(*dtaList[94:122], ids)
        #self.aux.dtaLam().transctUpdateMsvLaminas(*dtaList[94:122], cliente)
        
        # --- REFILADO ---
        self.aux.dtaRef().transctUpdateMsvRefilID(*dtaList[122:150], ids)
        #self.aux.dtaRef().transctUpdateMsvRefil(*dtaList[122:150], cliente)
        
        # --- CONVERSION ---
        self.aux.dtaConvrs().transctUpdateMsvCnvrsID(*dtaList[150:174], ids)
        #self.aux.dtaConvrs().transctUpdateMsvCnvrs(*dtaList[150:174], cliente)#'''