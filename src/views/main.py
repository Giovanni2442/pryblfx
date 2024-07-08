from tkinter import *
from tkinter import Misc, ttk
#from ttkthemes import ThemedStyle # type: ignore
from VentanaMain.vtnMain import *

class appMain:
    root = Tk()     # raiz : Objeto de tipo Frame de la clase Tk()
    root.wm_title("ventana de pruebas")
    app = vtnMain(root)     # Pasando el frame a la clase ventana, que en este caso es la instancia root
    app.mainloop()


if __name__ == "__main__":
    re = appMain()
    re()


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
