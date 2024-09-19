from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

class Insrt_FichaVentas():
    def __init__(self,estd):
        self.estd = estd
        self.aux = MtdsAuxPdf(self.estd)
        #self.estd = estd    # Estado del boton si es Insert o Update
    
    def pdfFichVent(self,page,tpl):
        txt = "VALUE"
        
        #### TABLA FichaTecnica ####
            # id_producto
        page.insert_text(   
            (930, 135),
            #text= tpl[0][0].value.upper(),  #Id_PrindCard
            text=self.aux.txtAux(tpl,0,0),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # cliente
        page.insert_text(   
            (915, 84),
            #text=  tpl[0][1].value.upper(),
            text=self.aux.txtAux(tpl,0,1),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # Producto
        page.insert_text(   
            (304, 135),
            #text = tpl[0][4].value.upper(),
            text=self.aux.txtAux(tpl,0,2),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # fecha_elav
        page.insert_text(   
            (915, 58),
            #text =  tpl[0][2].value.upper(),
            text=self.aux.txtAux(tpl,0,3),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

        '''    # fecha_Rev
        page.insert_text(   
            (653, 82),
            #text =  tpl[0][3].value.upper(),
            text=self.aux.txtAux(tpl,0,4),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )'''

        ################################

        #### -- TABLA VENTAS -- #####

            # Asesor Comercial
        page.insert_text(   
            (320, 178),
            #text =  tpl[1][0].value.upper(),
            text=self.aux.txtAux(tpl,1,0),
            color=(0, 0, 0),
            fontsize=7,
            fontname="Helvetica-Bold"
        )

            # Tipo de empaque
        page.insert_text(   
            (320, 192),
            #text =  tpl[1][1].value.upper(),
            text=self.aux.txtAux(tpl,1,1),
            color=(0, 0, 0),
            fontsize=7,
            fontname="Helvetica-Bold"
        )

            # Producto laminado
        page.insert_text(   
            (320, 206),
            #text =  tpl[1][2].value.upper(),
            text=self.aux.txtAux(tpl,1,2),
            color=(0, 0, 0),
            fontsize=7,
            fontname="Helvetica-Bold"
        )

        # Estructura del producto
        page.insert_text(   
            (233, 219),
            #text = tpl[1][3].value.upper(),
            text=self.aux.txtAux(tpl,1,3),
            color=(0, 0, 0),
            fontsize=7,
            fontname="Helvetica-Bold"
        )

        # producto que se empaca
        page.insert_text(   
            (320, 234),
            #text = tpl[1][4].value.upper(),
            text=self.aux.txtAux(tpl,1,4),
            color=(0, 0, 0),
            fontsize=7,
            fontname="Helvetica-Bold"
        )

    