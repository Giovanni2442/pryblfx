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
        
        #'''        # --- INSERCIÓN POR REBANADAS ---   
            # --- FICHA --- 
        self.dataTbl.post_data(*self.tpl2[:5])
            # --- VENTAS ---
        self.dataTbl.post_dataVentas(self.tpl2[0],*self.tpl2[5:10])
            # --- EXTRUCIÓN ---
        self.dtaExtr.postExtr(self.tpl2[0],*self.tpl2[10:24])                  # TABLA PADRE EXTEUSIÓN
        self.dtaExtr.postCalibrePel_Tolr(self.tpl2[0],*self.tpl2[24:26])       # Calibre_Tol
        self.dtaExtr.postAnchoBob_Tolr(self.tpl2[0],*self.tpl2[26:28])         # Calibre_Tol
        self.dtaExtr.postAnchoCore_Tolr(self.tpl2[0],*self.tpl2[28:30])        # Calibre_Tol
        self.dtaExtr.postDiametroBob_Tolr(self.tpl2[0],*self.tpl2[30:32])      # Calibre_Tol
        self.dtaExtr.postPeso_Prom_Bob(self.tpl2[0],*self.tpl2[32:34])         # Calibre_Tol
        self.dtaExtr.postNum_BobCama_CamTam(self.tpl2[0],*self.tpl2[34:36])    # Calibre_Tol
        self.dtaExtr.postPeso_prom_tarima(self.tpl2[0],*self.tpl2[36:38])      # Calibre_Tol
             # --- IMPRESION ---
        self.dtaImpr.postImprs(self.tpl2[0],*self.tpl2[38:57])                  # TABLA PADRE IMPRESION
        self.dtaImpr.postVldClr(self.tpl2[0],*self.tpl2[57:59])  
        self.dtaImpr.postCalMater_Tolr(self.tpl2[0],*self.tpl2[59:61])  
        self.dtaImpr.postAnchoBobImpr_Tolr(self.tpl2[0],*self.tpl2[61:63])  
        self.dtaImpr.postAnchoCore_TolrImpr(self.tpl2[0],*self.tpl2[63:65])  
        self.dtaImpr.postAnchoDiamBob_Tolr(self.tpl2[0],*self.tpl2[65:67])  
        self.dtaImpr.postPesoPromBob(self.tpl2[0],*self.tpl2[67:69])  
        self.dtaImpr.postNum_BobCama_CamaTarima(self.tpl2[0],*self.tpl2[69:71])  
        self.dtaImpr.postPeso_prom_tarimaImpr(self.tpl2[0],*self.tpl2[71:73]) 
            # --- LAMINADO ---
        self.dtaLam.postLam(self.tpl2[0],*self.tpl2[73:80])
        self.dtaLam.postMedidManga(self.tpl2[0],*self.tpl2[80:82])
        self.dtaLam.postAnchoCore_TolrLam(self.tpl2[0],*self.tpl2[82:84])
        self.dtaLam.postDiametro_GrosCore(self.tpl2[0],*self.tpl2[84:86])
        self.dtaLam.postDiametro_Bob_Tolr(self.tpl2[0],*self.tpl2[86:88])

                        # - Material Impreso -
        self.dtaLam.postMaterial_Impreso(self.tpl2[0],*self.tpl2[88:90]) 
        self.dtaLam.postCalibrePelic_Tolr(self.tpl2[0],*self.tpl2[90:92]) 
        self.dtaLam.postAnchoBob_TolrMtrlr(self.tpl2[0],*self.tpl2[92:94])  
                        # - Lam #1 -
        self.dtaLam.postMaterial_Laminar_1(self.tpl2[0],*self.tpl2[94:97])  
        self.dtaLam.postCalibrePelic_TolrLam1(self.tpl2[0],*self.tpl2[97:99])  
        self.dtaLam.postAnchoBob_TolrLam1(self.tpl2[0],*self.tpl2[99:101])
                        # - Lam #2 -
        self.dtaLam.postMaterial_Laminar_2(self.tpl2[0],*self.tpl2[101:104])  
        self.dtaLam.postCalibrePelic_TolrLam2(self.tpl2[0],*self.tpl2[104:106])  
        self.dtaLam.postAnchoBob_TolrLam2(self.tpl2[0],*self.tpl2[106:108])  
                         # - Lam #3 -
        self.dtaLam.postMaterial_Laminar_3(self.tpl2[0],*self.tpl2[108:111])  
        self.dtaLam.postCalibrePelic_TolrLam3(self.tpl2[0],*self.tpl2[111:113])  
        self.dtaLam.postAnchoBob_TolrLam3(self.tpl2[0],*self.tpl2[113:115])  
                         # - Lam #4 -
        self.dtaLam.postMaterial_Laminar_4(self.tpl2[0],*self.tpl2[115:118])  
        self.dtaLam.postCalibrePelic_TolrLam4(self.tpl2[0],*self.tpl2[118:120])  
        self.dtaLam.postAnchoBob_TolrLam4(self.tpl2[0],*self.tpl2[120:122])  
            # --- REFILADO ---
        self.dtaRef.postRefilado(self.tpl2[0],*self.tpl2[122:135])
        self.dtaRef.postAnchoFinalBob_TolrRef(self.tpl2[0],*self.tpl2[135:137])
        self.dtaRef.postMetrosBobRefil_Tolr(self.tpl2[0],*self.tpl2[137:139])
        self.dtaRef.postDiamBobRefil_Tolr(self.tpl2[0],*self.tpl2[139:141])
        self.dtaRef.postPesoNet_Prom_Bob(self.tpl2[0],*self.tpl2[141:143])
        self.dtaRef.postNum_BobCama_CamTamRefil(self.tpl2[0],*self.tpl2[143:145])
        self.dtaRef.postPeso_prom_tarimaRefil(self.tpl2[0],*self.tpl2[145:147])
            # --- CONVERSION ---
        self.dtaConvrs.postConversion(self.tpl2[0],*self.tpl2[147:162]) 
        self.dtaConvrs.postMedidEmpq(self.tpl2[0],*self.tpl2[162:164]) 
        self.dtaConvrs.postNumBlts_CajsCmas_CmasTarim(self.tpl2[0],*self.tpl2[164:166])
        self.dtaConvrs.postNumBlts_CajsTarim(self.tpl2[0],*self.tpl2[166:168]) #'''

        return self.tpl2

