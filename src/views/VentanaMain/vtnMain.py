from flet import *

import flet as ft

class ejemplo(UserControl):
    def __init__(self,page):
        super().__init__()

        self.page = page

        def changePosition(e):
            id = e.control.data.controls[0].value
            print(id)

            # Podemos navegar en los Controls de un gidwed y acceder a su Indice
            controls = [
                self.bottom_bar.content.controls[0],
                self.bottom_bar.content.controls[1],
                self.bottom_bar.content.controls[2],
            ]

            for i , cnt in enumerate(controls):
                cnt.content.controls[1].visible = (1 == id)
                cnt.bgcolor = e.control.data.controls[1].value if i == id else "white"
                page.controls[0].bgcolor = e.control.data.controls[1].value
            page.update()


        self.bottom_bar = Container(
            bgcolor="white",
            padding=20,
            bottom=10,
            left=10,
            right=10,
            width=page.window_width,
            border_radius=border_radius.only(
                bottom_left=30,
                bottom_right=30,    
            ),
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                # Este es el Tab 1
                Container(
                    bgcolor="Red",
                    border_radius=30,
                    padding=10,
                    animate=animation.Animation(300,"cubic"),
                    content= Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                        IconButton(icon="home",
                            icon_size=30,
                            data=Row([Text(0),Text("red200")]),
                            on_click=changePosition
                        ),
                        Text("Home",size=20,visible=True)
                    ])
                ),
                # Este es el Tab 2
                Container(
                    bgcolor="white",
                    border_radius=30,
                    padding=10,
                    animate=animation.Animation(300,"cubic"),
                    content= Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                        IconButton(icon="person",
                            icon_size=30,
                            data=Row([Text(1),Text("yellow")]),
                            on_click=changePosition
                        ),
                        Text("person",size=20,visible=False)
                    ])
                ),
                # Este es el tab 3
                Container(
                    bgcolor="white",
                    border_radius=30,
                    padding=10,
                    animate=animation.Animation(300,"cubic"),
                    content= Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                        IconButton(icon="bookmark",
                            icon_size=30,
                            data=Row([Text(1),Text("blue200")]),
                            on_click=changePosition
                        ),
                        Text("bookmark",size=20,visible=False)
                    ])
                ),
            ])
        )

        self.elmnst2 = Container(
            padding=10,
            animate=animation.Animation(300,"easeIn"),
            alignment=alignment.center,
            content=Text("Agregar aqui los elementos!")
        )

        self.elements = Container(
            width=page.window_width,
            height=page.window_height,
            bgcolor="red",
            animate=animation.Animation(300,"easeIn"),
            content=Stack([
                self.elmnst2,
                self.bottom_bar
            ])
        )

    def build(self):
        return self.elements

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.window_width = 500
    page.add(ejemplo(page))

app(main)
'''
# Main
app(main)'''
