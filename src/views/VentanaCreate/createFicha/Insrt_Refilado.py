class Instr_Refilado():
    def __init__(self):
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

    # Inserción de datos de la tabla Refilado
    def pdfRefil(self,page):

        # PROCESO A REALIZAR: (DOBLADO, REFILADO, AMBOS)
        page.insert_text(   
            (685, 827),
            text= "PROCESO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO FINAL DE BOBINA AL REFILARSE/DOBLARSE Y TOLERANCIA (CM)
        page.insert_text(   
            (685, 840),
            text= "ANCHO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ACABADO DE LA BOBINA: (COMERCIAL/ESPEJO)
        page.insert_text(   
            (685, 855),
            text= "ACABADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE CORE Y TOLERANCIA
        page.insert_text(   
            (685, 869),
            text= "CORE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # GROSOR DE CORE: (10 MM / OTRO)
        page.insert_text(   
            (685, 883),
            text= "GROSOR",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # FIGURA DE EMBOBINADO  EN REFILAD
        page.insert_text(   
            (685, 898),
            text= "FIGURA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # POR METROS, DIÁMETRO O PESO?
        page.insert_text(   
            (685, 913),
            text= "METROS",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # METROS POR BOBINA AL REFILARSE/DOBLARSE Y TOLERANCIA
        page.insert_text(   
            (685, 926),
            text= "REFILARSE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # DIAMETRO DE BOBINA AL
        page.insert_text(   
            (685, 940),
            text= "DIAMETRO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (685, 954),
            text= "MÁXIMO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # SEÑALIZACIÓN DE EMPALME:
        page.insert_text(   
            (685, 968),
            text= "SEÑALIZACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: (HORIZONTAL/ VERTICAL)
        page.insert_text(   
            (685, 981),
            text= "ORIENTACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMPAQUE PARA BOBINA:
        page.insert_text(   
            (685, 996),
            text= "EMPAQUE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESAR PRODUCTO POR:
        page.insert_text(   
            (685, 1012),
            text= "PESAR",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text(   
            (685, 1025),
            text= "NETO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ETIQUETADO: 
        page.insert_text(   
            (685, 1039),
            text= "ETIQUETADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA
        page.insert_text(   
            (685, 1053),
            text= "BOBINAS POR CAMA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BOBINAS EN TARIMA
        page.insert_text(   
            (685, 1068),
            text= "TARIMA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO POR TARIMA
        page.insert_text(   
            (685, 1082),
            text= "PROMEDIO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA LLEVARA EMPLAYE:
        page.insert_text(   
            (685, 1096),
            text= "EMPLAYE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text(   
            (685, 1110),
            text= "FLEJADA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text(   
            (685, 1110),
            text= "FLEJADA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )
