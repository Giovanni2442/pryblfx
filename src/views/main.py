from flet import *

class menu(UserControl):
    def __init__(self,page):
        super().__init__()

        self.page = page

    def viewiD(slef,e):
        id = e.control.data.value
        pass

        self.menu = Container(
            bgcolor="blue",
            #height=200,
            padding=5,
            animate=animation.Animation(300,"cubic"),
            content= Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        IconButton(
                            icon=icons.NOTIFICATION_ADD,
                            icon_size=25
                        ),
                    ),
                    
                    Container(
                        IconButton(
                            icon=icons.NOTIFICATION_ADD,
                            icon_size=25
                        ),
                    ),

                    Container(
                        IconButton(
                            icon=icons.NOTIFICATION_ADD,
                            icon_size=25
                        ),
                    ),
                ]
            )
        )

        self.frameMain = Container(
            bgcolor="yellow",
            padding=3,
            content= Column(
                controls=[
                    self.menu
                ]
            )
        )
        self.pru = Container(
            bgcolor="Red",
            height=100,
            expand=True
        )

    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(menu(page)) 

app(main)
    
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
