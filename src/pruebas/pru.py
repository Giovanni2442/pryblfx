from flet import *

class ejemplo():
    def __init__(self):
        super().__init__(expand=True)

        self.cnt1 = Container(
            bgcolor="Red",
            width=100,
            height=100
        )

    def build(self):
        return self.cnt1

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(ejemplo(page))

app(main)

'''def subMnuLam():
    dic = {
        "1" : "11",
        "2" : "22"
    }
    print(dic["1"])

def ciclo():
    for i in range(4):
        print(i)


ciclo()
#subMnuLam()

# -- CALAR --
self.psProm = Dropdown(
            label="Peso Neto Promedio De : ",
            hint_text="Peso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("BULTO"),
                dropdown.Option("CAJA"),
                dropdown.Option(
                    TextField(
                        label="Cantidad de Piezas por Paquete",
                        border= InputBorder.OUTLINE,
                        border_color="Black",
                        label_style=TextStyle(color="Black",italic=True),
                    ))
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )'''