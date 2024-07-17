from flet import * 
from src.views.VentanaCreate.InptFich_Vents import InptsTable
from src.app.filExcel.filtroExcel import filter

class Inpst_ImprDig():
    def __init__(self,page):
        super().__init__()

    ### INPUTS DE LA TABLA IMPRECIÓN DIGITAL ###

    ### SECCIÓN 1 ###
        self.mtrlImpr = TextField(
            label="Material Imprimir",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.dnjReq = TextField(
            label="Dinaje Requerido",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.calMtrlImpr_Tol = PopupMenuButton(
            Text("Calibre de Material a Imprimir y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.anchBobImpr_Tol = PopupMenuButton(
            Text("Ancho de Bobina a Imprimir y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.grosorCore = TextField(
            label="Grosor de Core",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.anchCore_Tol = PopupMenuButton(
            Text("Ancho de Core y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        