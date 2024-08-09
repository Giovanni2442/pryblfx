from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

# Insertar Valores del formulario EXTRUSION al pdf 
class Insrt_Extr():
    def __init__(self):
        self.vl = 7

        #Metodo Auxiliar
        self.aux = MtdsAuxPdf()
    
    # Tabla de Extrusion
    def pdfExtru(self,page,tpl):
        vl = 9

        # Tipo de material a Extruir
        page.insert_text( 
            (320, 271),
            text= tpl[2][0].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # Dinaje Requerido
        page.insert_text( 
            (320, 285),
            text= tpl[2][1].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # FÓRMULA CON LA QUE SE EXTRUIRÁ LA BOBINA
        page.insert_text( 
            (320, 299),
            text= tpl[2][2].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PIGMENTO DE PELÍCULA: (SI (especificar color), N/A)
        page.insert_text(   
            (320, 313),
            text= tpl[2][3].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text( 
            (320, 328),
            text = self.aux.pru(tpl,2,14,"±","% GAUGUES"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE BOBINA: 
        page.insert_text( 
            (320, 341),
            text= tpl[2][4].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE TRATADO: 
        page.insert_text( 
            (320, 355),
            text= tpl[2][5].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE BOBINA Y TOLERANCIA 
        page.insert_text( 
            (320, 369),
            #text= tpl[2][15].items[0].content.controls[1].value.upper(),
            text = self.aux.pru(tpl,2,15,"+","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE CORE Y TOLERANCIA 
        page.insert_text( 
            (320, 384),
            #text= tpl[2][16].items[0].content.controls[1].value.upper(),
            text = self.aux.pru(tpl,2,16,"+","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA
        page.insert_text( 
            (320, 398),
            #text= tpl[2][17].items[0].content.controls[1].value.upper(),
            text = self.aux.pru(tpl,2,17,"+","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text( 
            (320, 412),
            text= tpl[2][6].value,
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: (HORIZONTAL/ VERTICAL)
        page.insert_text( 
            (320, 426),
            text= tpl[2][7].value,
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE EMPAQUE PARA BOBINA: (EMPLAYE / BOLSA / N/A)
        page.insert_text( 
            (320, 440),
            text= tpl[2][8].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESAR PRODUCTO POR: (TARIMA / BOBINA / AMBOS)
        page.insert_text( 
            (320, 454),
            text= tpl[2][9].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text( 
            (320, 468),
            #text= tpl[2][18].items[0].content.controls[1].value.upper(),
            text = self.aux.pru(tpl,2,18,"+","KG"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ETIQUETADO
        page.insert_text( 
            (320, 482),
            text= tpl[2][10].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA
        page.insert_text( 
            (320, 496),
            #text= tpl[2][19].items[0].content.controls[1].value.upper(),
            text = self.aux.pru(tpl,2,19,"X","PZ"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS EN TARIMA
        page.insert_text( 
            (320, 511),
            text= tpl[2][11].value,
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO POR TARIMA
        page.insert_text( 
            (320, 525),
            #text= tpl[2][20].items[0].content.controls[1].value.upper(),
            text = self.aux.pru(tpl,2,20,"+","KG"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        
        # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A)
        page.insert_text( 
            (320, 539),
            text= tpl[2][12].value,
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text( 
            (320, 553),
            text= tpl[2][13].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # Numero de Bobinas en Tarima
        page.insert_text( 
            (320, 553),
            text= tpl[2][13].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )
