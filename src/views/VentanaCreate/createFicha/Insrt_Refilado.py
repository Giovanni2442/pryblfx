from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

class Instr_Refilado():
    def __init__(self):
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

        #Metodo Auxiliar
        self.aux = MtdsAuxPdf()

    # Inserción de datos de la tabla Refilado
    def pdfRefil(self,page,tpl):

        # PROCESO A REALIZAR: (DOBLADO, REFILADO, AMBOS)
        page.insert_text(   
            (685, 827),
            text= str(tpl[5][0].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO FINAL DE BOBINA AL REFILARSE/DOBLARSE Y TOLERANCIA (CM)
        page.insert_text(   
            (685, 840),
            #text= tpl[5][13].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,5,14,"+","CM"),
            #text = "VALORE ERRONEO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ACABADO DE LA BOBINA: (COMERCIAL/ESPEJO)
        page.insert_text(   
            (685, 855),
            text= str(tpl[5][1].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE CORE Y TOLERANCIA
        page.insert_text(   
            (685, 869),
            #text= tpl[5][19].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,5,20,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # GROSOR DE CORE: (10 MM / OTRO)
        page.insert_text(   
            (685, 883),
            text= str(tpl[5][2].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # FIGURA DE EMBOBINADO  EN REFILAD
        page.insert_text(   
            (685, 898),
            text= str(tpl[5][3].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # La bobina se refilara POR METROS, DIÁMETRO O PESO?
        page.insert_text(   
            (685, 913),
            text=  tpl[5][4].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # METROS POR BOBINA AL REFILARSE/DOBLARSE Y TOLERANCIA
        page.insert_text(   
            (685, 926),
            #text= tpl[5][14].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,5,15,"+","MTRS"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # DIAMETRO DE BOBINA AL
        page.insert_text(   
            (685, 940),
            #text= tpl[5][15].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,5,16,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (685, 954),
            text= str(tpl[5][5].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # SEÑALIZACIÓN DE EMPALME:
        page.insert_text(   
            (685, 968),
            text= tpl[5][6].value.upper(),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: (HORIZONTAL/ VERTICAL)
        page.insert_text(   
            (685, 981),
            text= str(tpl[5][7].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMPAQUE PARA BOBINA:
        page.insert_text(   
            (685, 996),
            text= str(tpl[5][8].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESAR PRODUCTO POR:
        page.insert_text(   
            (685, 1012),
            text= str(tpl[5][9].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text(   
            (685, 1025),
            #text= tpl[5][16].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,5,17,"+","KG"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ETIQUETADO: 
        page.insert_text(   
            (685, 1039),
            text= str(tpl[5][10].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA
        page.insert_text(   
            (685, 1053),
            #text= tpl[5][17].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,5,18,"X","PZ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BOBINAS EN TARIMA
        page.insert_text(   
            (685, 1068),
            text= str(tpl[5][13].value),
            #text="VALOR ERRONEO!",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO POR TARIMA
        page.insert_text(   
            (685, 1082),
            #text= tpl[5][18].items[0].content.controls[1].value,
            text = self.aux.pru(tpl,5,19,"+","KG"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA LLEVARA EMPLAYE:
        page.insert_text(   
            (685, 1096),
            text= str(tpl[5][11].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text(   
            (685, 1110),
            text= str(tpl[5][12].value),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

