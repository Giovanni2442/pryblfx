from flet import *


class eje2(UserControl)
    
    
        self.frame1 = Container(
            bgcolor="red",
            width=150,
            height=150,
            padding=5,
            margin=0,
            alignment=alignment.center,
            content= Row(
                controls=[
                    Text("Hola"),
                    Text("Hola"),
                    Text("Hola"),
                ],
            )
        )

        self.frame2 = Container(
            bgcolor="blue",
            width=150,
            height=150,
            padding=10,
            margin=0,
            alignment=alignment.center,
            content= Row(
                controls=[
                    Text("Hola"),
                    Text("Hola"),
                    Text("Hola"),
                ],
            )
        )