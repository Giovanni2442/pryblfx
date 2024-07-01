from typing import Any, List
import flet as ft
from flet import *          # Se importa todos los componentes de la Libreria "flet"
from Controllers.appTable import Controllers

class UI(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

    # --- COMPONENTES ---
        self.color_teal = "teal"

        #Input de busqueda del PrindCard
        self.InptPrindCard = TextField(
            label="Buscar PridCard",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True)
        )

        self.InptClienteSimple = TextField(
            label="Buscar Cliente",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True)
        )

        self.InptClienteMasiva = TextField(
            label="Buscar Cliente",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="black",italic=True)
        )

        #Table
        self.data_table = DataTable(
            border= border.all(2,"purple"),
            columns=[
                DataColumn(Text("PRIND_CARD",color="whithe",weight="bold")),
                DataColumn(Text("CLIENTE",color="whithe",weight="bold")),
                DataColumn(Text("PRODUCTO",color="whithe",weight="bold")),
                DataColumn(Text("FECHA",color="whithe",weight="bold")),
                DataColumn(Text("HERRAMIENTAS",color="whithe",weight="bold"))
            ]
        )

        # Muestra los datos de la base de datos
        def showData(self):
           # return self.dataTable.rows = []
           pass
    #-----------------------------

    # --- CONTENEDORES,FRAMES ETC ... ---
        # Contenedor para el filtrado
        self.cntFiltPrinf = Container(
            expand=True,
            bgcolor="#222222",
            border_radius=5,
            padding=10,
            content= Row(
                controls=[
                    #Contenedor de busquedas masivas por ciente
                    Container(
                        expand=True,
                        bgcolor=self.color_teal,
                        border_radius=10,
                        padding=8,
                        content= Column(
                            controls=[  
                                Container(
                                    Text("Busqueda Masiva : ",color="whithe"),
                                    #self.InptPrindCard,
                                    alignment=alignment.center,
                                    bgcolor="black",
                                    border_radius=5
                                ),
                                self.InptClienteMasiva
                            ]
                        )
                    ),
                    # Contenedor de Busquedas Simples
                    Container(
                        expand=True,
                        bgcolor= self.color_teal,
                        border_radius=10,
                        padding=8,
                        alignment = alignment.center_right,
                        content= Column(
                            controls=[
                                Container( 
                                    Text("Buscar por : ",color="whithe"),
                                    #self.InptPrindCard,
                                    alignment=alignment.center,
                                    bgcolor="black",
                                    border_radius=5
                                ),
                                
                                self.InptPrindCard,
                                self.InptClienteSimple
                            ]
                        )
                    )
                ]
            ),
        )

        self.cntTable = Container(
            bgcolor="#222222",  # Cambiado a azul para distinguir visualmente
            border_radius=10,
            alignment=alignment.top_center,
            expand=True,
            padding=10,
            content= Column( 
                expand=True,
                scroll="auto",
                controls=[
                    self.data_table
                ]
            )
        )

        self.frameMain = Container(
            bgcolor="black",
            border_radius=10,
            padding=2,
            content=Column(
                    controls=[
                        self.cntFiltPrinf,
                        self.cntTable
                    ],
                ),
        )
        self.container = ResponsiveRow(
            controls=[
                self.frameMain
            ]
        )
        

        self.controls.append(self.container)  # Añadir el contenedor al layout del UserControl

    
def main(page: Page):       #   page : Es el Frame o la ventana de la Aplicación
    page.window_min_height = 200
    page.window_min_width = 200
    page.theme_mode = ThemeMode.DARK
    page.padding = 5
    page.add(UI(page))

ft.app(main)