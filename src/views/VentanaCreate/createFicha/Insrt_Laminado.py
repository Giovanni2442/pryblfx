class Insrt_Laminado():
    def __init__(self):
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

    def pdfLam(self,page):

        # ESTRUCTURA DEL PRODUCTO
        page.insert_text(   
            (555, 177),
            text= "ESTRUCTURA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # --- MATERIAL IMPRESO ---
        page.insert_text(   
            (685, 192),
            text= "MATERIAL",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 206),
            text= "CALIBRE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 220),
            text= "ANCHO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO: 
        page.insert_text(   
            (685, 234),
            text= "TRATADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # --- MATERIAL PARA LAMINAR Nº1 ---
        page.insert_text(   
            (685, 248),
            text= "LAMINAR Nº1",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 262),
            text= "CALIBRE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 276),
            text= "ANCHO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 290),
            text= "TRATADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 305),
            text= "LAMINACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )


        # --- MATERIAL PARA LAMINAR Nº2 ---
        page.insert_text(   
            (685, 319),
            text= "LAMINAR Nº2",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 333),
            text= "CALIBRE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 346),
            text= "ANCHO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 361),
            text= "TRATADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 375),
            text= "LAMINACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )


        # --- MATERIAL PARA LAMINAR Nº3 ---
        page.insert_text(   
            (685, 389),
            text= "LAMINAR Nº3",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 403),
            text= "CALIBRE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 417),
            text= "ANCHO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 432),
            text= "TRATADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 446),
            text= "LAMINACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # --- MATERIAL PARA LAMINAR Nº4 ---
        page.insert_text(   
            (685, 460),
            text= "LAMINAR Nº4",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 473),
            text= "CALIBRE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 488),
            text= "ANCHO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 504),
            text= "TRATADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 518),
            text= "LAMINACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # --- GENERAL CONTINUACIÓN ---
        # MEDIDA DE LA MANGA PARA TRANSFERENCIA
        page.insert_text(   
            (685, 532),
            text= "MANGA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE CORE Y TOLERANCIA
        page.insert_text(   
            (685, 545),
            text= "CORE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # DIÁMETRO Y GROSOR DE CORE
        page.insert_text(   
            (685, 559),
            text= "DIÁMETRO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 573),
            text= "BOBINA",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (685, 586),
            text= "MÁXIMO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ORIENTACIÓN DE BOBINA EN RACK
        page.insert_text(   
            (685, 602),
            text= "ORIENTACIÓN",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMPAQUE PARA BOBINA
        page.insert_text(   
            (685, 616),
            text= "EMPAQUE",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ETIQUETADO
        page.insert_text(   
            (685, 630),
            text= "ETIQUETADO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESAR PRODUCTO POR: (TARIMA / BOBINA / AMBOS)
        page.insert_text(   
            (685, 644),
            text= "PESAR",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text(   
            (685, 658),
            text= "NETO",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )


        






        