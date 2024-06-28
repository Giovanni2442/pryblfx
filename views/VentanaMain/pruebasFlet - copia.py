from typing import Any, List
import flet as ft
from flet import *          # Se importa todos los componentes de la Libreria "flet"

class UI(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = "teal"

        self.cntEncabezado = Container(
            expand=True,
            bgcolor="green",
            border_radius=10,
            padding=10
        )

        # Contenedor para el filtrado
        self.cntFiltPrinf = Container(
            expand=True,
            bgcolor="green",
            border_radius=10,
            padding=10,
            content= Row(
                controls=[
                    Container(
                        expand=True,
                        bgcolor="blue",
                        border_radius=10,
                        padding=5,
                        content= Column(
                            controls=[
                                
                                    
                            ]
                        )
                    ),
                    Container(
                        expand=True,
                        bgcolor="blue",
                        border_radius=10,
                    ),
                    Container(
                        expand=True,
                        bgcolor="blue",
                        border_radius=10,
                        padding=5,
                        alignment = alignment.center_right,
                        content= Column(
                            controls=[
                                Container( 
                                    Text("Buscar Por:",color="black"),
                                    padding=5,
                                    bgcolor="#83AC9E",
                                    border_radius=10
                                ),
                                Container(
                                    padding=5,
                                    border_radius=10,
                                    bgcolor="#83AC9E",
                                    content= Row(
                                        controls=[
                                            IconButton(icon=icons.SEARCH),
                                            TextField(
                                                hint_text="PrindCard..",
                                                border=InputBorder.NONE
                                            )
                                        ]
                                    )
                                ),

                                Container(
                                    padding=5,
                                    border_radius=10,
                                    bgcolor="#83AC9E",
                                    content= Row(
                                        controls=[
                                            IconButton(icon=icons.SEARCH),
                                            TextField(
                                                hint_text="Cliente..",
                                                border=InputBorder.NONE
                                            )
                                        ]
                                    )
                                )
                                
                            ]
                        )
                    )
                ]
            ),
        )

        self.cntTable = Container(
            bgcolor="green",  # Cambiado a azul para distinguir visualmente
            border_radius=10,
            expand=True,
            #border=20
            #col=6  # Ocupa 6 columnas de las 12 disponibles
        )

        self.frameMain = Container(
            bgcolor=self.color_teal,
            border_radius=10,
            padding=5,
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
    page.add(UI(page))

ft.app(main)