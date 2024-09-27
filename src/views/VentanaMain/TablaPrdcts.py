# -- HACER UNA TABLA DONDE MUESTRE
# TODOS LOS DATOS QUE TIENE LAS FICHAS
# EN CADA PROCESO -- #

from flet import * 

class TablaPrdcts(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)
        self.color_teal = "teal50"
        
    # --- HEADER DE LA TABLA ---
        self.cntFiltPrinf = Container(
            #expand=True,
            bgcolor= colors.BLACK12,
            border_radius=0,
            alignment= alignment.center,
            padding=0,
            content= Row(
                controls=[
                    # Contenedor de Busquedas Simples
                    Container(
                        expand=True,
                        bgcolor= colors.WHITE,
                        border_radius=0,
                        padding=8,
                    
                        alignment=alignment.center,
                        content= Column(
                            controls=[
                                Container(
                                    #bgcolor="Red",
                                    height=25,
                                    content=
                                        TextButton(
                                            icon=icons.HOME,
                                            #icon=lambda e: self.prbtn(e)
                                            icon_color="#405d44",
                                            on_click=self.toggle_menu
                                        #bgcolor="RED",
                                        )
                                ),
                                Container( 
                                    Image(src="venv/src/views/VentanaMain/logotipo/logo.png", width=200, height=200),
                                    #Text("FICHA TECNICA",color=colors.BLACK38,theme_style=TextThemeStyle.TITLE_SMALL),
                                    border=border.only(bottom=border.BorderSide(0.5, colors.BLACK87)),
                                    #expand=True,
                                    #self.InptPrindCard,
                                    alignment=alignment.center,
                                    
                                    shadow=BoxShadow(
                                        spread_radius=-35,   # No se expande hacia dentro ni hacia afuera
                                        blur_radius=95,    # Incrementa el desenfoque para suavizar la sombra
                                        offset=Offset(0,0),  # Desplaza la sombra más hacia abajo
                                        color="#283c29",
                                        blur_style=ShadowBlurStyle.NORMAL
                                    ),

                                    height=50,
                                    #bgcolor=colors.AMBER,
                                    border_radius=0
                                ),
                                # BUSCADORES...
                                #self.InptPrindCard,
                                #self.InptClienteSimple,
                                # Se coloca en un contenedor para centar
                                Container(
                                    #expand=True,
                                    alignment=alignment.bottom_left,
                                    #bgcolor="yellow",
                                    padding=5,
                                    border_radius=3,
                                    content= Row(
                                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        controls= [
                                            Text("PrindCards",
                                                color=colors.BLACK38,
                                                theme_style=TextThemeStyle.TITLE_LARGE,
                                                font_family="Calibri",italic=True),
                                            #self.BtnCreate,
                                            #self.BtnpRU,
                                            #self.BtnCreate2
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            ),
        )

    # --- TABLA DE PRODUCTOS ---
        self.Table = DataTable(
            #border= border.all(2,"purple"),
            #border_radius=2,
            #expand=True,
            #bgcolor="#146364",
            bgcolor="#263b27",
            data_row_color = colors.WHITE70,
            #border_radius=border_radius.only(top_left=10,top_right=10),
            vertical_lines= BorderSide(0.5,color=colors.WHITE24),
            columns=[
                DataColumn(Text("VENTAS",color=colors.WHITE,weight="bold")),
                DataColumn(Text("EXTRUSION",color=colors.WHITE,weight="bold")),
                DataColumn(Text("IMPRESION",color=colors.WHITE,weight="bold")),
                DataColumn(Text("LAMINADO",color=colors.WHITE,weight="bold")),
                DataColumn(Text("REFILADO",color=colors.WHITE,weight="bold")),
                DataColumn(Text("CONVERSION",color=colors.WHITE,weight="bold"))
            ],
        )

    # --- CONTENEDOR DE TABLA DE PRODUCTOS --- 
        self.TblPrdcts = Container(
            bgcolor= colors.RED,  # Cambiado a azul para distinguir visualmente
            height=200,
            #scroll="auto",
            border_radius=0,
            alignment=alignment.top_center,
            expand=True,
            padding=5,
            margin= margin.only(left=0,right=0,top=-5,bottom=0),
            content= Column( 
                expand=True,
                #scroll="auto",
                controls=[
                    Row(
                        scroll="ALWAYS",  # Habilita el scroll horizontal
                        controls=[
                            self.Table 
                        ]
                    )     
                ]
            )
        )
        
        self.mnuBar = Container(
            expand=True,
            #visible=False,
            bgcolor="#ddddddcf",
            margin=margin.only(top=50),
            #window = 90
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

        # Colocar los frames en forma de columna
        self.frameMain = Container(
            bgcolor= colors.BLACK12,
            border_radius=10,
            padding=8,
            content=Column(
                    controls=[
                        #self.mnuBar,         # MENU LATERAL DE PRUEBAS
                        self.cntFiltPrinf,
                        #self.cntTable
                    ],
                ),
        )
        # Hacer responsiva los framaes en forma de Fila
        self.container = ResponsiveRow(
            controls=[
                self.frameMain,
                self.TblPrdcts
            ]
        )

    def toggle_menu(self, e):       
        #print(self.mnuBar.content.controls[0].width)
        self.mnuBar.width = 290 if self.mnuBar.width == 0 else 0
        
        #self.mnuBar.content.controls[0].width = 200 if self.mnuBar.content.controls[0].width == 0 else 0
        #self.mnuBar.gbcolor = "Red" if self.mnuBar.bgcolor == "Yellow" else "Yellow"
         # Si no está en el overlay, lo añadimos
        
        self.page.overlay.append(self.mnuBar)
        self.page.update()

    # IMPORTANTE : Retorna todos los Gidwts del promama
    def build(self):    
        return self.container

'''
def main(page: Page):
    page.window_min_height = 200
    page.window_min_width = 200

    #page.theme_mode = ThemeMode.DARK
    page.padding = 0
    #page.adaptive = True
    page.add(TablaPrdcts(page))

app(main)'''