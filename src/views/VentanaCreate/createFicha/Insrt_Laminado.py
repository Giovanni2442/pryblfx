from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

class Insrt_Laminado():
    def __init__(self,estd):

        self.estd = estd
        self.aux = MtdsAuxPdf(self.estd)

        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

        
    def pdfLam(self,page,tpl):

        # ESTRUCTURA DEL PRODUCTO
        page.insert_text(   
            (555, 177),
            #text="NULL",
            #text= tpl[4][0].value.upper(),
            text=self.aux.txtAuxLamGen(tpl,4,0,0,0,1),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )


        # --- MATERIAL IMPRESO ---
        page.insert_text(   
            (685, 192),
            #text= tpl[4][11][0].value.upper(),
            text=self.aux.txtAuxLamins(tpl,4,11,0,0,5,0), # txtAuxLamins
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO: 
        page.insert_text(   
            (685, 234),
            #text= str(tpl[4][11][1].value),
            text= str(self.aux.txtAuxLamins(tpl,4,11,1,0,5,1)), # txtAuxLamins
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 206),
            #text= tpl[4][11][2].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,11,2,0,6,0,0,6,1,"±","µ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 220),
            #text= tpl[4][11][3].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,11,3,0,7,0,0,7,1,"±","CM"),
            #text = self.aux.pruLam(tpl,4,11,3,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

       
        # --- MATERIAL PARA LAMINAR Nº1 ---
        page.insert_text(   
            (685, 248),
            #text= tpl[4][12][0].value.upper(),
            text=self.aux.txtAuxLamins(tpl,4,12,0,1,0,1), # txtAuxLamins
            #text="NULL",
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 290),
            #text= str(tpl[4][12][1].value),
            text=str(self.aux.txtAuxLamins(tpl,4,12,1,1,0,2)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )
  
        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 305),
            #text= str(tpl[4][12][2].value),
            text=self.aux.txtAuxLamins(tpl,4,12,2,1,0,3),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 262),
            #text= tpl[4][12][3].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,12,3,1,1,0,1,1,1,"±","µ"),
            #text = self.aux.pruLam(tpl,4,12,3,"+","µ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 276),
            #text= tpl[4][12][4].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,12,4,1,2,0,1,2,1,"±","CM"),
            #text = self.aux.pruLam(tpl,4,12,4,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )




        # --- MATERIAL PARA LAMINAR Nº2 ---
        page.insert_text(   
            (685, 319),
            #text= tpl[4][13][0].value.upper(),
            text=self.aux.txtAuxLamins(tpl,4,13,0,1,3,0),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 361),
            #text= str(tpl[4][13][1].value),
            text= str(self.aux.txtAuxLamins(tpl,4,13,1,1,3,1)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 375),
            #text= str(tpl[4][13][2].value),
            text= str(self.aux.txtAuxLamins(tpl,4,13,2,1,3,2)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 333),
            #text= tpl[4][13][3].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,13,3,1,4,0,1,4,1,"±","µ"),
            #text = self.aux.pruLam(tpl,4,13,3,"+","µ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 346),
            #text= tpl[4][13][4].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,13,4,1,5,0,1,5,1,"±","CM"),
            #text = self.aux.pruLam(tpl,4,13,4,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )


        # --- MATERIAL PARA LAMINAR Nº3 ---
        page.insert_text(   
            (685, 389),
            #text= tpl[4][14][0].value.upper(),
            text=self.aux.txtAuxLamins(tpl,4,14,0,1,6,0),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 432),
            #text= str(tpl[4][14][1].value),
            text=str(self.aux.txtAuxLamins(tpl,4,14,1,1,6,1)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 446),
            #text= str(tpl[4][14][2].value),
            text= str(self.aux.txtAuxLamins(tpl,4,14,2,1,6,2)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 403),
            #text= tpl[4][14][3].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,14,3,1,7,0,1,7,1,"±","µ"),
            #text = self.aux.pruLam(tpl,4,14,3,"+","µ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 417),
            #text= tpl[4][14][4].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,14,4,1,8,0,1,8,1,"±","CM"),
            #text = self.aux.pruLam(tpl,4,14,4,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        

        # --- MATERIAL PARA LAMINAR Nº4 ---
        page.insert_text(   
            (685, 460),
            #text= tpl[4][15][0].value.upper(),
            text= self.aux.txtAuxLamins(tpl,4,15,0,1,9,0),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE TRATADO:
        page.insert_text(   
            (685, 504),
            #text= str(tpl[4][15][1].value),
            text= str(self.aux.txtAuxLamins(tpl,4,15,1,1,9,1)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE LAMINACIÓN 
        page.insert_text(   
            (685, 518),
            #text= str(tpl[4][15][2].value),
            text= str(self.aux.txtAuxLamins(tpl,4,15,2,1,9,2)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (685, 473),
            #text= tpl[4][15][3].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,15,3,1,10,0,1,10,1,"±","µ"),
            #text = self.aux.pruLam(tpl,4,15,3,"+","µ"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 488),
            #text= tpl[4][15][4].items[0].content.controls[1].value,
            text = self.aux.frmlTolLaminas(tpl,4,15,4,1,11,0,1,11,1,"±","CM"),
            #text = self.aux.pruLam(tpl,4,15,4,"+","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # --- GENERAL CONTINUACIÓN ---
        # MEDIDA DE LA MANGA PARA TRANSFERENCIA
        page.insert_text(   
            (685, 532),
            #text= tpl[4][7].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,4,7,"+","CM"),
            text=self.aux.frmlTolLamGen(tpl,4,7,0,1,0,0,1,1,"±","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ANCHO DE CORE Y TOLERANCIA
        page.insert_text(   
            (685, 545),
            #text= tpl[4][8].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,4,8,"+","CM"),
            text = self.aux.frmlTolLamGen(tpl,4,8,0,2,0,0,2,1,"±","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # DIÁMETRO Y GROSOR DE CORE
        page.insert_text(   
            (685, 559),
            #text= tpl[4][9].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,4,9,"+","CM"),
            text = self.aux.frmlTolLamGen(tpl,4,9,0,3,0,0,3,1,"±","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (685, 573),
            #text= tpl[4][10].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,4,10,"+","CM"),
            text = self.aux.frmlTolLamGen(tpl,4,10,0,4,0,0,4,1,"±","CM"),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )


        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (685, 586),
            #text= str(tpl[4][1].value),
            text= str(self.aux.txtAuxLamGen(tpl,4,1,0,0,2)),
            #text= str(self.aux.txtAux2(tpl,4,1,0,2)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ORIENTACIÓN DE BOBINA EN RACK
        page.insert_text(   
            (685, 602),
            #text= tpl[4][2].value.upper(),
            text= str(self.aux.txtAuxLamGen(tpl,4,2,0,0,3)),
            #text= self.aux.txtAux2(tpl,4,2,0,3),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # TIPO DE EMPAQUE PARA BOBINA
        page.insert_text(   
            (685, 616),
            #text= tpl[4][3].value.upper(),
            #text= self.aux.txtAux2(tpl,4,3,0,4),
            text= str(self.aux.txtAuxLamGen(tpl,4,3,0,0,4)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # ETIQUETADO
        page.insert_text(   
            (685, 630),
            #text= tpl[4][4].value.upper(),
            #text= self.aux.txtAux2(tpl,4,4,0,5),
            text= str(self.aux.txtAuxLamGen(tpl,4,4,0,0,5)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESAR PRODUCTO POR: (TARIMA / BOBINA / AMBOS)
        page.insert_text(   
            (685, 644),
            #text= tpl[4][5].value.upper(),
            #text= self.aux.txtAux2(tpl,4,5,0,6),
            text= str(self.aux.txtAuxLamGen(tpl,4,5,0,0,6)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text(   
            (685, 658),
            #text= str(tpl[4][6].value),
            #text= self.aux.txtAux2(tpl,4,6,0,7),
            text= str(self.aux.txtAuxLamGen(tpl,4,6,0,0,7)),
            color=self.clr,
            fontsize=self.vl,
            fontname=self.fnt
        )
