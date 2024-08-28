from flet import *
#from src.Controllers.appdb import appDb
#'''
#from src.conectDataBase.testConectDb import dbpool
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appFichVent import appFichVent
from src.Controllers.appExtr import appExtr
from src.Controllers.appImpr import appImpr
from src.Controllers.appLam import appLam
from src.Controllers.appRef import appRef
from src.Controllers.appConvrs import appConvrs#'''

class appInserts():
    def __init__(self,page):
        super().__init__()

        #self.data = appDb()

        #self.connectPool = dbpool()
        #self.conex = self.connectPool.get_connection()
        #self.cursor = self.conex.cursor()

        #self.page = page
        self.filter = filter().vrfPrintCard
        self.b1 = True
        self.page = page
        self.dataTbl = appFichVent
        self.dtaExtr = appExtr
        self.dtaImpr = appImpr
        self.dtaLam = appLam
        #self.dtaRef = appRef()
        #self.dtaConvrs = appConvrs()

        self.tpl = []
        self.tpl2 = []
        self.bnd = 0


    # RECOLECTOR DE DATOS PARA CADA ENTRADA
    def qryPost(self,tpl):                     # Recorre las listas de Inputs para colocarlas en una lista
        #vle = tpl[2][0].items[0].content.controls[1].value
        for indx,i in enumerate(tpl):       # Recorre las listas de Inputs
            for j in i:                     # Recorre los valores de cada lista
                if isinstance(j, list):     # Verifica si el valor de la lista hay listas, para colocar los valores en la lista padre
                    for f in j:             # Recorre la sub lista desde el indice
                        if isinstance( f, PopupMenuButton):
                            for m in f.items:
                                txtFld = m.content.controls[1]
                                #print("--- **** ", txtFld.label)
                                self.tpl2.append(txtFld.value)
                        else:
                            #print(f" --xx {f.label}")
                            self.tpl2.append(f.value)
                        #print("-->" ,f) 
                    continue
                if isinstance(j, PopupMenuButton):
                    for k in j.items:
                        txtFld = k.content.controls[1]
                        #print("--- **** ", txtFld.label)
                        self.tpl2.append(txtFld.value)
                else:
                    #print(f" --xx {inx}  : {j.label} : {j.value}")
                    self.tpl2.append(j.value)
            
        #-- INSERCIÓN --#
        #je = self.tpl2[162:164] # Laminación
        #print(je)
        #print(self.tpl2)
        #print(je)

        print("-----------> : " ,self.tpl2[10:24])

        #'''
                # --- INSERCIÓN POR REBANADAS ---   

            # --- FICHA --- 
        #self.dataTbl.post_data(*self.tpl2[:5])

            # --- VENTAS ---
        #self.dataTbl.post_dataVentas(self.tpl2[0],*self.tpl2[5:10])
        #self.data.dtaFichVen.transactInsrtFichVents(*self.tpl2[:10])
            # --- PRUEBAS FICHA / VENTAS  
        self.dataTbl().transactInsrtFichVents(*self.tpl2[:10])
        
            # --- EXTRUCIÓN ---
        self.dtaExtr().transctInsertExtrs(self.tpl2[0],*self.tpl2[10:38])
        
            # --- IMPRESION ---
        self.dtaImpr().transIsertImprs(self.tpl2[0],*self.tpl2[38:73])
        
            # --- LAMINACIÓN ---
        self.dtaLam().transctInsertLam(self.tpl2[0],*self.tpl2[73:94])
        self.dtaLam().transctInsertLmns(self.tpl2[0],*self.tpl2[94:122])

        #'''
         

