from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

class Insrt_Convrs():
    def __init__(self) -> None:
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

        #Metodo Auxiliar
        self.aux = MtdsAuxPdf()
    
    def pdfConvrs(self,page,tpl):
        # tpl[5][18].items[0].content.controls[1].value
        # MEDIDA DEL EMPAQUE: (ANCHO Y ALTO) 
        page.insert_text(   
            (1045, 177),
            #text= tpl[6][16].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,6,16,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMPAQUE
        page.insert_text(   
            (1045, 191),
            text= tpl[6][0].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE SELLO
        page.insert_text(   
            (1045, 206),
            text= tpl[6][1].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE ACABADO
        page.insert_text(   
            (1045, 220),
            text= tpl[6][2].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EL PRODUCTO LLEVA PERFORACIÓN: (APLICA / N/A)
        page.insert_text(   
            (1045, 234),
            text= tpl[6][3].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CANTIDAD DE  PERFORACIONES
        page.insert_text(   
            (1045, 248),
            text= tpl[6][4].value,
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EL PRODUCTO LLEVA SUAJE: (APLICA / N/A)
        page.insert_text(   
            (1045, 262),
            text= tpl[6][5].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE SUAJE:
        page.insert_text(   
            (1045, 275),
            text= tpl[6][6].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EMPACADO DE PRODUCTO: (KILEADO / PIEZAS / GRANEL)
        page.insert_text(   
            (1045, 290),
            text= tpl[6][7].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CANTIDAD DE PIEZAS POR PAQUETE 
        page.insert_text(   
            (1045, 304),
            text= tpl[6][8].value,
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMBALAJE  
        page.insert_text(   
            (1045, 319),
            text= tpl[6][9].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # MEDIDA DEL EMBALAJE:  
        page.insert_text(   
            (1045, 334),
            text= tpl[6][10].value,
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

         # PESAR PRODUCTO POR: (TARIMA / BULTO / CAJA) 
        page.insert_text(   
            (1045, 350),
            text= tpl[6][11].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO DE: (BULTO / CAJA/ OTRO)  
        page.insert_text(   
            (1045, 363),
            text= tpl[6][12].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ETIQUETADO  
        page.insert_text(   
            (1045, 376),
            text= tpl[6][13].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BULTOS O CAJAS POR CAMA Y CAMAS POR TARIMA   (
        page.insert_text(   
            (1045, 391),
            #text= tpl[6][17].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,6,17,"+","PZ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BULTOS O CAJAS POR TARIMA 
        page.insert_text(   
            (1045, 405),
            #text= tpl[6][18].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,6,18,"±","PZ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO POR TARIMA: 
        page.insert_text(   
            (1045, 418),
            #text= tpl[6][19].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,6,19,"±","KG"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A) 
        page.insert_text(   
            (1045, 432),
            text= tpl[6][14].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A) 
        page.insert_text(   
            (1045, 447),
            text= tpl[6][15].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )