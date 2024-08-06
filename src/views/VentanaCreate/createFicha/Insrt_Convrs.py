class Insrt_Convrs():
    def __init__(self) -> None:
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

    def pdfConvrs(self,page):

        # MEDIDA DEL EMPAQUE: (ANCHO Y ALTO) 
        page.insert_text(   
            (1045, 177),
            text= "MEDIDA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMPAQUE
        page.insert_text(   
            (1045, 191),
            text= "EMPAQUE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE SELLO
        page.insert_text(   
            (1045, 206),
            text= "SELLO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE ACABADO
        page.insert_text(   
            (1045, 220),
            text= "ACABADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EL PRODUCTO LLEVA PERFORACIÓN: (APLICA / N/A)
        page.insert_text(   
            (1045, 234),
            text= "PERFORACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CANTIDAD DE  PERFORACIONES
        page.insert_text(   
            (1045, 248),
            text= "CANTIDAD",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EL PRODUCTO LLEVA SUAJE: (APLICA / N/A)
        page.insert_text(   
            (1045, 262),
            text= "SUAJE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE SUAJE:
        page.insert_text(   
            (1045, 275),
            text= "TIPO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # EMPACADO DE PRODUCTO: (KILEADO / PIEZAS / GRANEL)
        page.insert_text(   
            (1045, 290),
            text= "EMPACADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CANTIDAD DE PIEZAS POR PAQUETE 
        page.insert_text(   
            (1045, 304),
            text= "PIEZAS",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMBALAJE  
        page.insert_text(   
            (1045, 319),
            text= "EMBALAJE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # MEDIDA DEL EMBALAJE:  
        page.insert_text(   
            (1045, 334),
            text= "MEDIDA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

         # PESAR PRODUCTO POR: (TARIMA / BULTO / CAJA) 
        page.insert_text(   
            (1045, 350),
            text= "PESAR",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO DE: (BULTO / CAJA/ OTRO)  
        page.insert_text(   
            (1045, 363),
            text= "PROMEDIO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ETIQUETADO  
        page.insert_text(   
            (1045, 376),
            text= "ETIQUETADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BULTOS O CAJAS POR CAMA Y CAMAS POR TARIMA   (
        page.insert_text(   
            (1045, 391),
            text= "CAMA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BULTOS O CAJAS POR TARIMA 
        page.insert_text(   
            (1045, 405),
            text= "BULTOS",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # NUMERO DE BULTOS O CAJAS POR TARIMA 
        page.insert_text(   
            (1045, 405),
            text= "BULTOS",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        ) 

        # PESO NETO PROMEDIO POR TARIMA: 
        page.insert_text(   
            (1045, 418),
            text= "NETO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A) 
        page.insert_text(   
            (1045, 432),
            text= "EMPLAYE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A) 
        page.insert_text(   
            (1045, 447),
            text= "FLEJADA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )