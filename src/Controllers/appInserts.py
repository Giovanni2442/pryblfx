from flet import *
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appFichVent import appFichVent
from src.Controllers.appExtr import appExtr
from src.Controllers.appImpr import appImpr
from src.Controllers.appLam import appLam
from src.Controllers.appRef import appRef
from src.Controllers.appConvrs import appConvrs

class appInserts():
    def __init__(self,page):
        super().__init__()

        #self.page = page
        self.filter = filter().vrfPrintCard
        self.b1 = True
        self.page = page
        self.dataTbl = appFichVent()
        self.dtaExtr = appExtr()
        self.dtaImpr = appImpr()
        self.dtaLam = appLam()
        self.dtaRef = appRef()
        self.dtaConvrs = appConvrs()

        self.tpl = []
        self.tpl2 = []
        self.bnd = 0


    # Ejecuta POST hacia todas las tablas de lo formularios
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

        print("-----------> : " ,self.tpl2[150:165])
        
                # --- INSERCIÓN POR REBANADAS ---   
            # --- FICHA --- 
        self.dataTbl.post_data(*self.tpl2[:5])
            # --- VENTAS ---
        self.dataTbl.post_dataVentas(self.tpl2[0],*self.tpl2[5:10])
            # --- EXTRUCIÓN ---
        self.dtaExtr.postExtr(self.tpl2[0],*self.tpl2[10:25])                  # TABLA PADRE EXTEUSIÓN
        self.dtaExtr.postCalibrePel_Tolr(self.tpl2[0],*self.tpl2[25:27])       # Calibre_Tol
        self.dtaExtr.postAnchoBob_Tolr(self.tpl2[0],*self.tpl2[27:29])         # Calibre_Tol
        self.dtaExtr.postAnchoCore_Tolr(self.tpl2[0],*self.tpl2[29:31])        # Calibre_Tol
        self.dtaExtr.postDiametroBob_Tolr(self.tpl2[0],*self.tpl2[31:33])      # Calibre_Tol
        self.dtaExtr.postPeso_Prom_Bob(self.tpl2[0],*self.tpl2[33:35])         # Calibre_Tol
        self.dtaExtr.postNum_BobCama_CamTam(self.tpl2[0],*self.tpl2[35:37])    # Calibre_Tol
        self.dtaExtr.postPeso_prom_tarima(self.tpl2[0],*self.tpl2[37:39])      # Calibre_Tol
             # --- IMPRESION ---
        self.dtaImpr.postImprs(self.tpl2[0],*self.tpl2[39:58])                  # TABLA PADRE IMPRESION
        self.dtaImpr.postVldClr(self.tpl2[0],*self.tpl2[58:60])  
        self.dtaImpr.postCalMater_Tolr(self.tpl2[0],*self.tpl2[60:62])  
        self.dtaImpr.postAnchoBobImpr_Tolr(self.tpl2[0],*self.tpl2[62:64])  
        self.dtaImpr.postAnchoCore_TolrImpr(self.tpl2[0],*self.tpl2[64:66])  
        self.dtaImpr.postAnchoDiamBob_Tolr(self.tpl2[0],*self.tpl2[66:68])  
        self.dtaImpr.postPesoPromBob(self.tpl2[0],*self.tpl2[68:70])  
        self.dtaImpr.postNum_BobCama_CamaTarima(self.tpl2[0],*self.tpl2[70:72])  
        self.dtaImpr.postPeso_prom_tarimaImpr(self.tpl2[0],*self.tpl2[72:74]) 
            # --- LAMINADO ---
        self.dtaLam.postLam(self.tpl2[0],*self.tpl2[74:81])
        self.dtaLam.postMedidManga(self.tpl2[0],*self.tpl2[81:83])
        self.dtaLam.postAnchoCore_TolrLam(self.tpl2[0],*self.tpl2[83:85])
        self.dtaLam.postDiametro_GrosCore(self.tpl2[0],*self.tpl2[85:87])
        self.dtaLam.postDiametro_Bob_Tolr(self.tpl2[0],*self.tpl2[87:89])

                        # - Material Impreso -
        self.dtaLam.postMaterial_Impreso(self.tpl2[0],*self.tpl2[89:91]) 
        self.dtaLam.postCalibrePelic_Tolr(self.tpl2[0],*self.tpl2[91:93]) 
        self.dtaLam.postAnchoBob_TolrMtrlr(self.tpl2[0],*self.tpl2[93:95])  
                        # - Lam #1 -
        self.dtaLam.postMaterial_Laminar_1(self.tpl2[0],*self.tpl2[95:98])  
        self.dtaLam.postCalibrePelic_TolrLam1(self.tpl2[0],*self.tpl2[98:100])  
        self.dtaLam.postAnchoBob_TolrLam1(self.tpl2[0],*self.tpl2[100:102])
                        # - Lam #2 -
        self.dtaLam.postMaterial_Laminar_2(self.tpl2[0],*self.tpl2[102:105])  
        self.dtaLam.postCalibrePelic_TolrLam2(self.tpl2[0],*self.tpl2[105:107])  
        self.dtaLam.postAnchoBob_TolrLam2(self.tpl2[0],*self.tpl2[107:109])  
                         # - Lam #3 -
        self.dtaLam.postMaterial_Laminar_3(self.tpl2[0],*self.tpl2[109:112])  
        self.dtaLam.postCalibrePelic_TolrLam3(self.tpl2[0],*self.tpl2[112:114])  
        self.dtaLam.postAnchoBob_TolrLam3(self.tpl2[0],*self.tpl2[114:116])  
                         # - Lam #4 -
        self.dtaLam.postMaterial_Laminar_4(self.tpl2[0],*self.tpl2[116:119])  
        self.dtaLam.postCalibrePelic_TolrLam4(self.tpl2[0],*self.tpl2[119:121])  
        self.dtaLam.postAnchoBob_TolrLam4(self.tpl2[0],*self.tpl2[121:123])  
            # --- REFILADO ---
        self.dtaRef.postRefilado(self.tpl2[0],*self.tpl2[123:137])
        self.dtaRef.postAnchoFinalBob_TolrRef(self.tpl2[0],*self.tpl2[137:139])
        self.dtaRef.postMetrosBobRefil_Tolr(self.tpl2[0],*self.tpl2[139:141])
        self.dtaRef.postDiamBobRefil_Tolr(self.tpl2[0],*self.tpl2[141:143])
        self.dtaRef.postPesoNet_Prom_Bob(self.tpl2[0],*self.tpl2[143:145])
        self.dtaRef.postNum_BobCama_CamTamRefil(self.tpl2[0],*self.tpl2[145:147])
        self.dtaRef.postPeso_prom_tarimaRefil(self.tpl2[0],*self.tpl2[147:149])
        self.dtaRef.postAnchCre_Tol(self.tpl2[0],*self.tpl2[149:151])       # -- AREGLAR ESTE PEDO, QUE FALTA XD
        
            # --- CONVERSION ---
        self.dtaConvrs.postConversion(self.tpl2[0],*self.tpl2[151:166]) 
        self.dtaConvrs.postMedidEmpq(self.tpl2[0],*self.tpl2[166:168]) 
        self.dtaConvrs.postNumBlts_CajsCmas_CmasTarim(self.tpl2[0],*self.tpl2[168:170])
        self.dtaConvrs.postNumBlts_CajsTarim(self.tpl2[0],*self.tpl2[170:172]) #'''
        self.dtaConvrs.postPsPromTam(self.tpl2[0],*self.tpl2[172:174]) #'''

        return self.tpl2

