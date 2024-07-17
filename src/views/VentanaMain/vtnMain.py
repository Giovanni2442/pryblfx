from flet import * 
class pr(UserControl):
    def __init__(self,page):
        super().__init__()

        self.page = page
        self.qt = ""

        self.id_product = TextField(
            label="PrindCard",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            #on_change= self.vl()       # Traba con la expreción regular del input
        )

        self.cnt1 = Container(
            width=400,
            height=100,
            bgcolor="green",
            padding=5,
            content= self.id_product
        )
    
    def update(self,id):
        self.id_product.value = id
        id2 = id
        self.id_product.value = id2
        self.update()
        print(id2)

    def vl(self, e=None, id=None):
        #print(id)
        self.id_product.value = id
        #print(self.id_product.value)
        #self.update()

    def main(self):
        self.frmMain = Container(
            bgcolor="yellow",
            padding=10,
            #on_click=self.vl(),
            content=Column([
                self.cnt1,
            ])
        )
        return self.frmMain

    def build(self):
        return self.main()
    
def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(pr(page))

#app(main)

    