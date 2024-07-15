from flet import *

import datetime
import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))       

    page.add(
        ft.ElevatedButton(
            "Pick date",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2000, month=12, day=1),
                    last_date=datetime.datetime(year=2064, month=12, day=1),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,  
                )
            ),
        )
    )


ft.app(target=main)
'''
from flet import Container, Row, Column, Label, margin

class MiClase:
    def __init__(self):
        self.color_teal = "teal"  # Suponiendo que tienes definido el color teal

        # Función que maneja el cambio de tamaño de la ventana
        def resize_handler(width):
            if width < 300:  # Ejemplo: Cambiar a Column si el ancho es menor que 300 píxeles
                self.content = Column(
                    controls=[
                        Label(text="Elemento 1"),
                        Label(text="Elemento 2"),
                        Label(text="Elemento 3")
                    ]
                )
            else:
                self.content = Row(
                    controls=[
                        Label(text="Elemento 1"),
                        Label(text="Elemento 2"),
                        Label(text="Elemento 3")
                    ]
                )

        # Creación del Container inicial con Row
        self.cntHeader2 = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content=Row(
                controls=[
                    Label(text="Elemento 1"),
                    Label(text="Elemento 2"),
                    Label(text="Elemento 3")
                ]
            )
        )

        # Llamar a resize_handler con el ancho inicial de la ventana
        initial_width = 500  # Aquí debes obtener el ancho inicial de la ventana
        resize_handler(initial_width)

# Ejemplo de uso
mi_clase = MiClase()
'''
