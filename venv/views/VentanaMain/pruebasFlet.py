from typing import Any, List
import flet as ft
from flet import *          # Se importa todos los componentes de la Libreria "flet"

class UI(UserControl):
    def __init__(self,page):
        super().__init__()      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = 0

        self.Nav_Cont = Container(
            bgcolor=self.color_teal,
            border_radius=10,

        )
        
        self.container = ResponsiveRow()
    
    def build(self):
        return self.container
    

def main(page: Page):       #   page : Es el Frame o la ventana de la Aplicación
    page.window_min_height = 200
    page.window_min_width = 200
    page.theme_mode = ThemeMode.SYSTEM
    page.add(UI(page))
    def addLabel():
        lblText = Text(
            value="Este es un Label",
            color="green",
            font_family="Arial")
        page.controls.append(lblText)      
        page.window_center()
        page.update()

    def btnClick(e):
        if not inptName.value:
            inptName.error_text = "No se ha Ingresado texto!"
            page.update()
        else:
            text = inptName.value
            page.clean()
            page.add(
                Text(f"Hello {text}!")
            )

    inptName = TextField(
            label="Preciónar !",
            color="red",
            border_radius = 10
        )


# --- Agregar Widgets ---
    page.add(
        #inptName,
        #ElevatedButton("Click me!", on_click=btnClick)
    )
        
ft.app(main)