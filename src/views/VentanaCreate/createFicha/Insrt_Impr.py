from src.views.VentanaCreate.createFicha.pdfAux import MtdsAuxPdf

class Insrt_Impr():
    def __init__(self,estd):
        self.vl = 7
        self.estd = estd
        self.aux = MtdsAuxPdf(self.estd)

    # Tabla de Extrusion
    def pdfImpr(self,page,tpl):
        # MATERIAL A IMPRIMIR
        page.insert_text( 
            (320, 693),
            #text= tpl[3][0].value.upper(),
            text=self.aux.txtAux2(tpl,3,0,0,1),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold",
        )

        # DINAJE REQUERIDO PARA SU IMPRESIÓN
        page.insert_text(
            (320, 707),
            text=self.aux.txtAux2(tpl,3,1,0,2),
            #text= tpl[3][1].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # CALIBRE DEL MATERIAL A IMPRIMIR Y TOLERANCIA
        page.insert_text( 
            (320, 721),
            #text= tpl[3][20].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,3,20,"+","µ"),
            text = self.aux.frmlTol(tpl,3,20,2,0,2,1,"±","µ"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE BOBINA A IMPRIMIR Y TOLERANCIA 
        page.insert_text( 
            (320, 735),
            #text= tpl[3][21].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,3,21,"+","CM"),
            text = self.aux.frmlTol(tpl,3,21,3,0,3,1,"±","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # GROSOR DE CORE:  (10 MM / OTRO) 
        page.insert_text( 
            (320, 748),
            #text= str(tpl[3][2].value),
            text= str(self.aux.txtAux2(tpl,3,2,0,3)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE CORE Y TOLERANCIA  
        page.insert_text( 
            (320, 763),
            #text= tpl[3][22].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,3,22,"+","CM"),
            text = self.aux.frmlTol(tpl,3,22,4,0,4,1,"±","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )
        
        # DESARROLLO A IMPRIMIR (MANGA)  
        page.insert_text( 
            (320, 777),
            #text= str(tpl[3][3].value),
            text= str(self.aux.txtAux2(tpl,3,3,0,4)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # REPETICIONES AL EJE  
        page.insert_text( 
            (320, 792),
            #text= str(tpl[3][4].value),
            text= str(self.aux.txtAux2(tpl,3,4,0,5)),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # REPETICIONES AL DESARROLLO 
        page.insert_text( 
            (320, 806),
            #text= str(tpl[3][5].value),
            text= str(self.aux.txtAux2(tpl,3,5,0,6)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # CANTIDAD DE TINTAS A IMPRIMIR 
        page.insert_text( 
            (320, 820),
            #text= str(tpl[3][6].value),
            text= str(self.aux.txtAux2(tpl,3,6,0,7)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE IMPRESIÓN: (INTERNA/EXTERNA) 
        page.insert_text( 
            (320, 834),
            #text= tpl[3][7].value.upper(),
            text= str(self.aux.txtAux2(tpl,3,7,0,8)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE TINTAS A UTILIZAR 
        page.insert_text( 
            (320, 848),
            #text= tpl[3][8].value.upper(),
            text= str(self.aux.txtAux2(tpl,3,8,0,9)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE BARNIZ SOBRE LA IMPRESIÓN 
        page.insert_text( 
            (320, 862),
            #text= tpl[3][9].value.upper(),
            text= str(self.aux.txtAux2(tpl,3,9,0,10)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # FIGURA DE EMBOBINADO AL SALIR DE IMPRESIÓN (1,2,3,4,5,6,7,8)
        page.insert_text( 
            (320, 876),
            #text= str(tpl[3][10].value),
            text= str(self.aux.txtAux2(tpl,3,10,0,11)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # VALIDACIÓN DE COLOR POR
        page.insert_text( 
            (320, 891),
            #text= tpl[3][19].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,3,19,"±","DELTAS"),
            text = self.aux.frmlTol(tpl,3,19,1,0,1,1,"±","% DELTAS"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text( 
            (320, 906),
            #text= str(tpl[3][11].value),
            text= str(self.aux.txtAux2(tpl,3,11,0,12)),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE EMPAQUE PARA BOBINA
        page.insert_text( 
            (320, 920),
            #text= tpl[3][12].value.upper(),
            text= self.aux.txtAux2(tpl,3,12,0,13),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: 
        page.insert_text( 
            (320, 934),
            #text= tpl[3][13].value.upper(),
            text= self.aux.txtAux2(tpl,3,13,0,14),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESAR PRODUCTO POR:
        page.insert_text( 
            (320, 948),
            #text= tpl[3][14].value.upper(),
            text= self.aux.txtAux2(tpl,3,14,0,15),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA 
        page.insert_text( 
            (320, 962),
            #text= tpl[3][23].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,3,23,"+","CM"),
            text = self.aux.frmlTol(tpl,3,23,5,0,5,1,"±","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

         # PESO NETO PROMEDIO DE BOBINA  
        
        # PESO NETO PROMEDIO POR BOBINA
        page.insert_text( 
            (320, 976),
            #text= tpl[3][24].items[0].content.controls[1].value,      
            #text = self.aux.pru(tpl,3,24,"+","CM"),
            text = self.aux.frmlTol(tpl,3,24,6,0,6,1,"±","CM"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ETIQUETADO  
        page.insert_text( 
            (320, 991),
            text= self.aux.txtAux2(tpl,3,15,0,16),
            #text= tpl[3][15].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA   
        page.insert_text( 
            (320, 1005),
            #text= tpl[3][25].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,3,25,"X","PZ"),
            text = self.aux.frmlTol(tpl,3,25,7,0,7,1,"X","PZ"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS EN TARIMA    
        page.insert_text( 
            (320, 1019),
            text= str(self.aux.txtAux2(tpl,3,16,0,17)),
            #text= str(tpl[3][16].value),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO POR TARIMA   
        page.insert_text( 
            (320, 1032),
            #text= tpl[3][26].items[0].content.controls[1].value,
            #text = self.aux.pru(tpl,3,26,"±","KG"),
            text = self.aux.frmlTol(tpl,3,26,8,0,8,1,"±","KG"),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

         # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A)  
        
        # Tarima Emplaya
        page.insert_text( 
            (320, 1047),
            text= self.aux.txtAux2(tpl,3,17,0,18),
            #text= tpl[3][17].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text( 
            (320, 1061),
            text= self.aux.txtAux2(tpl,3,18,0,19),
            #text= tpl[3][18].value.upper(),
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )
