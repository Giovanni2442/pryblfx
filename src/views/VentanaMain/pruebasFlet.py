from typing import Any, List
import flet as ft
from flet import *          # Se importa todos los componentes de la Libreria "flet"

class UI(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = "teal"

        self.frame1 = Container(
            #Text("Este es el contenedor 1"),
            bgcolor=self.color_teal,
            border_radius=10,
            #col=1
            col={"sm": 4, "md": 12, "xl": 6}
        )
        self.frame2 = Container(
            #Text("Este es el contenedor 1"),
            bgcolor=self.color_teal,
            border_radius=10,
            col=6
            #col={"sm": 8, "md": 5, "xl": 2}
        )

        self.container = ResponsiveRow(             # 
            controls=[
                self.frame1,
                self.frame2
            ]
        )

        self.controls.append(self.container)  # Añadir el contenedor al layout del UserControl

    
def main(page: Page):       #   page : Es el Frame o la ventana de la Aplicación
    page.window_min_height = 200
    page.window_min_width = 200
    page.theme_mode = ThemeMode.DARK
    page.add(UI(page))

app(main)