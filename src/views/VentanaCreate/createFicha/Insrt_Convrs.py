from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

class Insrt_Convrs():
    def __init__(self,estd):
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

        self.estd = estd
        self.aux = MtdsAuxPdf(self.estd)
    
    def pdfConvrs(self,page,tpl):
        # tpl[5][18].items[0].content.controls[1].value
        # MEDIDA DEL EMPAQUE: (ANCHO Y ALTO) 
        page.insert_text(   
            (1045, 177),
            #text= tpl[6][16].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,6,16,"+","CM"),
            text = self.aux.frmlTol(tpl,6,16,1,0,1,1,"±","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMPAQUE
        page.insert_text(   
            (1045, 191),
            #text= tpl[6][0].value.upper(),
            text=self.aux.txtAux2(tpl,6,0,0,1),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE SELLO
        page.insert_text(   
            (1045, 206),
            #text= tpl[6][1].value.upper(),
            text=self.aux.txtAux2(tpl,6,1,0,2),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE ACABADO
        page.insert_text(   
            (1045, 220),
            #text= tpl[6][2].value.upper(),
            text=self.aux.txtAux2(tpl,6,2,0,3),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EL PRODUCTO LLEVA PERFORACIÓN: (APLICA / N/A)
        page.insert_text(   
            (1045, 234),
            #text= tpl[6][3].value.upper(),
            text=self.aux.txtAux2(tpl,6,3,0,4),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CANTIDAD DE  PERFORACIONES
        page.insert_text(   
            (1045, 248),
            #text= str(tpl[6][4].value),
            text= str(self.aux.txtAux2(tpl,6,4,0,5)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EL PRODUCTO LLEVA SUAJE: (APLICA / N/A)
        page.insert_text(   
            (1045, 262),
            #text= tpl[6][5].value.upper(),
            text=self.aux.txtAux2(tpl,6,5,0,6),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE SUAJE:
        page.insert_text(   
            (1045, 275),
            #text= tpl[6][6].value.upper(),
            text=self.aux.txtAux2(tpl,6,6,0,7),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EMPACADO DE PRODUCTO: (KILEADO / PIEZAS / GRANEL)
        page.insert_text(   
            (1045, 290),
            #text= tpl[6][7].value.upper(),
            text=self.aux.txtAux2(tpl,6,7,0,8),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CANTIDAD DE PIEZAS POR PAQUETE 
        page.insert_text(   
            (1045, 304),
            #text= str(tpl[6][8].value),
            text=str(self.aux.txtAux2(tpl,6,8,0,9)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMBALAJE  
        page.insert_text(   
            (1045, 319),
            #text= tpl[6][9].value.upper(),
            text=self.aux.txtAux2(tpl,6,9,0,10),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # MEDIDA DEL EMBALAJE:  
        page.insert_text(   
            (1045, 334),
            #text= str(tpl[6][10].value),
            text= str(self.aux.txtAux2(tpl,6,10,0,11)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

         # PESAR PRODUCTO POR: (TARIMA / BULTO / CAJA) 
        page.insert_text(   
            (1045, 350),
            #text= tpl[6][11].value.upper(),
            text=self.aux.txtAux2(tpl,6,11,0,12),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO DE: (BULTO / CAJA/ OTRO)  
        page.insert_text(   
            (1045, 363),
            #text= str(tpl[6][12].value),
            text=str(self.aux.txtAux2(tpl,6,12,0,13)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ETIQUETADO  
        page.insert_text(   
            (1045, 376),
            #text= tpl[6][13].value.upper(),
            text=self.aux.txtAux2(tpl,6,13,0,14),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BULTOS O CAJAS POR CAMA Y CAMAS POR TARIMA   (
        page.insert_text(   
            (1045, 391),
            #text= tpl[6][17].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,6,17,"+","PZ"),
            text = self.aux.frmlTol(tpl,6,17,2,0,2,1,"+","PZ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BULTOS O CAJAS POR TARIMA 
        page.insert_text(   
            (1045, 405),
            #text= tpl[6][18].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,6,18,"±","PZ"),
            text = self.aux.frmlTol(tpl,6,18,3,0,3,1,"±","PZ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO POR TARIMA: 
        page.insert_text(   
            (1045, 418),
            #text= tpl[6][19].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,6,19,"±","KG"),
            text = self.aux.frmlTol(tpl,6,19,4,0,4,1,"±","KG"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A) 
        page.insert_text(   
            (1045, 432),
            #text= tpl[6][14].value.upper(),
            text=self.aux.txtAux2(tpl,6,14,0,15),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A) 
        page.insert_text(   
            (1045, 447),
            #text= tpl[6][15].value.upper(),
            text=self.aux.txtAux2(tpl,6,15,0,16),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )