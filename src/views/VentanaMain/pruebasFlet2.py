'''from typing import Any, List
import flet as ft
from flet import *                                      # Se importa todos los componentes de la Libreria "flet"
from src.views.VentanaMain.cmntsTbl import cntTable     # Componentes para el frame de la Tabla
from src.Controllers.appTable import Controllers

class UI(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

    # --- COMPONENTES ---
        self.page = page  
        self.color_teal = "teal"
        self.tbl = cntTable(self.page)  # Se pasa el pagina actual
        self.dataTbl = Controllers()  #Accede a la información en la base de datos
    
        # --- INPUTS DE BUSQUEDA --- 
            # Busqueda del PrindCard
        self.InptPrindCard = TextField(
            label="Buscar PridCard",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True)
        )
            # Busqueda por cliente
        self.InptClienteSimple = TextField(
            label="Buscar Cliente",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True)
        )
            # Busqueda / cliente Masivo
        self.InptClienteMasiva = TextField(
            label="Buscar Cliente",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="black",italic=True)
        )

        # -----------------------------

    # --- CONTENEDORES,FRAMES ETC ... ---
        # --- FRAME FILTRADO ---
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
    
        # --- FRAME TABLE ---
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
                    #self.data_table
                    ResponsiveRow(
                        controls=[
                            self.tbl.Table.update()
                            #self.updateTable()
                        ]
                    )
                ]
            )
        )

    
        # Colocar los frames en forma de columna
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
    # -------------------------------------

        # Hacer responsiva los framaes en forma de Fila
        self.container = ResponsiveRow(
            controls=[
                self.frameMain
            ]
        )

    # IMPORTANTE : Retorna todos los Gidwts del promama
    def build(self):    
        return self.container

def main(page: Page):       #   page : Es el Frame o la ventana de la Aplicación
    page.window_min_height = 200
    page.window_min_width = 200
    page.theme_mode = ThemeMode.DARK
    page.padding = 5
    ui = UI(page)
    page.add(ui)
    page.update()
ft.app(main)
#pru()'''