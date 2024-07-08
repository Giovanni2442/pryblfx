from flet import *
import flet as ft

def main(page):
    table=ft.DataTable(
        border=ft.border.all(2, "red"),
        show_bottom_border=True,
        #columns 里必须添加 DataColumn 类型的控件
        columns=[
                ft.DataColumn(ft.Text("名字")),
                ft.DataColumn(ft.Text("电话")),
                ft.DataColumn(ft.Text("地址"), numeric=True),
            ],
        #rows 里必须添加 DataRow 类型的控件
        #DataRow 
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ])
            ]
        )
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    lv.controls.append(table)
    page.add(lv)
    def button_clicked(e):
        
        
        b=ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ])

        table.rows.append(b)
        page.update()
        print("按钮被点击")
    page.add(ft.ElevatedButton(text="添加一行数据",on_click=button_clicked,data=0))

ft.app(target=main)




'''
class ejemplo2(UserControl):
    def __init__(self,page):
        super().__init__()

        self.page = page

        self.frame1 = Container(
            bgcolor="red",
            width=150,
            height=150,
            padding=5,
            margin=0,
            alignment=alignment.center,
            content= Column(
                controls=[
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
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
            content= Column(
                controls=[
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
                ],
            )
        )

        self.cntBtn = Container(
            bgcolor="green",
            #width=150,
            #height=150,
            padding=10,
            margin=0,
            alignment=alignment.center,
            content=Column(
                controls=[
                    #Text(),
                    TextButton("Press Here!",
                        icon=icons.PLAY_CIRCLE_FILL_OUTLINED,
                        on_click= lambda _: self.page.go('/'))
                ]
                    
            )
        )

    # Colocar los frames en forma de columna
        self.frameMain = Container(
            bgcolor="yellow",
            border_radius=10,
            padding=10,
            content=Column(
                    alignment=alignment.center,
                    expand=False,
                    controls=[
                        self.frame1,
                        self.frame2,
                        self.cntBtn 
                    ],
                ),
        )


   # Construye todos los frames tiene el frame Main
    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(ejemplo2(page))

# Main
app(main)'''