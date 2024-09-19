from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

# Insertar Valores del formulario EXTRUSION al pdf 
class Insrt_Extr():
    def __init__(self,estd):
        self.estd = estd
        self.aux = MtdsAuxPdf(self.estd)
        self.vl = 7
     
    # Tabla de Extrusion
    def pdfExtru(self,page,tpl):
        vl = 9

        # Tipo de material a Extruir
        page.insert_text( 
            (320, 271),
            #text= tpl[2][0].value.upper(),
            text=self.aux.txtAux2(tpl,2,0,0,1),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # Dinaje Requerido
        page.insert_text( 
            (320, 285),
            #text= tpl[2][1].value.upper(),
            text=self.aux.txtAux2(tpl,2,1,0,2),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # FÓRMULA CON LA QUE SE EXTRUIRÁ LA BOBINA
        page.insert_text( 
            (320, 299),
            #text= tpl[2][2].value.upper(),
            text=self.aux.txtAux2(tpl,2,2,0,3),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PIGMENTO DE PELÍCULA: (SI (especificar color), N/A)
        page.insert_text(   
            (320, 313),
            #text= tpl[2][3].value.upper(),
            text=self.aux.txtAux2(tpl,2,3,0,4),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text( 
            (320, 328),
            text = self.aux.frmlTol(tpl,2,14,1,0,1,1,"±","% GAUGUES"),
            #text = self.aux.pru(tpl,2,14,"±","% GAUGUES"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE BOBINA: 
        page.insert_text( 
            (320, 341),
            text=self.aux.txtAux2(tpl,2,4,0,5),
            #text= tpl[2][4].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE TRATADO: 
        page.insert_text( 
            (320, 355),
            #text= tpl[2][5].value.upper(),
            text=self.aux.txtAux2(tpl,2,5,0,6),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE BOBINA Y TOLERANCIA 
        page.insert_text( 
            (320, 369),
            text = self.aux.frmlTol(tpl,2,15,2,0,2,1,"±","CM"),
            #text= tpl[2][15].items[0].content.controls[1].value.upper(),
            #text = self.aux.pru(tpl,2,15,"+","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE CORE Y TOLERANCIA 
        page.insert_text( 
            (320, 384),
            text = self.aux.frmlTol(tpl,2,16,3,0,3,1,"±","CM"),
            #text= tpl[2][16].items[0].content.controls[1].value.upper(),
            #text = self.aux.pru(tpl,2,16,"+","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA
        page.insert_text( 
            (320, 398),
            text = self.aux.frmlTol(tpl,2,17,4,0,4,1,"±","CM"),
            #text= tpl[2][17].items[0].content.controls[1].value.upper(),
            #text = self.aux.pru(tpl,2,17,"+","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text( 
            (320, 412),
            text= str(self.aux.txtAux2(tpl,2,6,0,7)),
            #text= str(tpl[2][6].value),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: (HORIZONTAL/ VERTICAL)
        page.insert_text( 
            (320, 426),
            text= str(self.aux.txtAux2(tpl,2,7,0,8)),
            #text= str(tpl[2][7].value),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE EMPAQUE PARA BOBINA: (EMPLAYE / BOLSA / N/A)
        page.insert_text( 
            (320, 440),
            text= self.aux.txtAux2(tpl,2,8,0,9),
            #text= tpl[2][8].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESAR PRODUCTO POR: (TARIMA / BOBINA / AMBOS)
        page.insert_text( 
            (320, 454),
            #text= tpl[2][9].value.upper(),
            text= self.aux.txtAux2(tpl,2,9,0,10),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text( 
            (320, 468),
            text = self.aux.frmlTol(tpl,2,18,5,0,5,1,"±","KG"),
            #text= tpl[2][18].items[0].content.controls[1].value.upper(),
            #text = self.aux.pru(tpl,2,18,"+","KG"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ETIQUETADO
        page.insert_text( 
            (320, 482),
            text= self.aux.txtAux2(tpl,2,10,0,11),
            #text= tpl[2][10].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA
        page.insert_text( 
            (320, 496),
            text = self.aux.frmlTol(tpl,2,19,6,0,6,1,"X","PZ"),
            #text= tpl[2][19].items[0].content.controls[1].value.upper(),
            #text = self.aux.pru(tpl,2,19,"X","PZ"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS EN TARIMA
        page.insert_text( 
            (320, 511),
            #text= str(tpl[2][11].value),
            text= str(self.aux.txtAux2(tpl,2,11,0,12)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO POR TARIMA
        page.insert_text( 
            (320, 525),
            text = self.aux.frmlTol(tpl,2,20,7,0,7,1,"±","KG"),
            #text= tpl[2][20].items[0].content.controls[1].value.upper(),
            #text = self.aux.pru(tpl,2,20,"+","KG"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A)
        page.insert_text( 
            (320, 539),
            #text= tpl[2][12].value,
            text= self.aux.txtAux2(tpl,2,12,0,13),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text( 
            (320, 553),
            text= self.aux.txtAux2(tpl,2,13,0,14),
            #text= tpl[2][13].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )
