from flet import * 

class MenuBar(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)
        self.color_teal = "teal50"


        # HEADER AND MENU
        self.header = Container(
            #expand =True,
            bgcolor="Red",
            #width=50,
            #height=50,  
            #alignment=alignment.center,
            padding=0,
            content=Column(
                #alignment=MainAxisAlignment.END,
                controls=[
                    Container(      #-- CONTENEDOR INICIO Y USUARIO --
                        #expand=True,
                        #height=100,
                        bgcolor=colors.WHITE,
                        #border=border.only(bottom=border.BorderSide(1, "#858585")),
                        margin=margin.only(bottom=-6,left=0,right=0,top=0),
                    
                        alignment=alignment.center,
                        content= Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    TextButton(
                                        icon=icons.MENU,
                                        icon_color="#405d44",
                                        on_click=self.toggle_menu
                                    #bgcolor="RED",
                                    )
                                ),

                                Container(
                                    IconButton(icon=icons.MENU,
                                               icon_color="violet",
                                               on_click=  lambda _: self.page.go('/prueba')), #Agregar el registro de usuarios
                                    #bgcolor="RED",
                                )            
                            ]
                        )
                    )
                ]
            )
        )

        self.mnuBar = Container(
            expand=True,
            #visible=False,
            bgcolor="yellow",
            margin=margin.only(top=50),
            #window = 90
            #height=200,
            padding=5,
            width=0,
            alignment=alignment.top_left,
            animate=animation.Animation(1000, AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN),
            content=Column(
                expand=False,
                #bgcolor="Blue",
                #alignment=MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        visible=True,
                        width=200,
                        height=30,
                        bgcolor="Blue",
                        content=TextButton("Button with icon", icon="chair_outlined")   
                    )                   
                ]  
            )
        )

        self.frameMain = Container(
            padding=8,
            #expand=True,
            border_radius=10,
            bgcolor="GREEN70",
            content=Column(
                controls=[
                    self.header
                    #self.mnuBar
                ]
            )
        )
        '''
        self.contResposive = ResponsiveRow(
            controls=[
                self.frameMain
            ]
        )
        '''

    def toggle_menu(self, e):       
        print(self.mnuBar.content.controls[0].width)
        self.mnuBar.width = 290 if self.mnuBar.width == 0 else 0
        
        #self.mnuBar.content.controls[0].width = 200 if self.mnuBar.content.controls[0].width == 0 else 0
        #self.mnuBar.gbcolor = "Red" if self.mnuBar.bgcolor == "Yellow" else "Yellow"
        self.page.overlay.append(self.mnuBar)
        self.page.update()

    def build(self):
        return self.frameMain

def main(page: Page):
    page.window_min_height = 200
    page.window_min_width = 200

    #page.theme_mode = ThemeMode.DARK
    page.padding = 0
    #page.adaptive = True
    page.add(MenuBar(page))

app(main)