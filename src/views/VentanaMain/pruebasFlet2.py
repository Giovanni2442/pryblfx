from typing import Any, List
import flet as ft
from flet import *          # Se importa todos los componentes de la Libreria "flet"
from src.Controllers.appTable import Controllers
#from Controllers.appTable import Controllers

def pru():
    db = Controllers().get_row_Table()
    print(db)
    #pass

class UI(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

    # --- COMPONENTES ---
        self.page = page  
        self.color_teal = "teal"
        self.dataTbl = Controllers().get_row_Table()  #Accede a la información en la base de datos
        self.select_row = None

        # --- INPUTS DE BUSQUEDA --- 
            # Busqueda del PrindCard
        self.InptPrindCard = TextField(
            label="Buscar PridCard",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True)
        )
            # Busqueda por cliente
        self.InptClienteSimple = TextField(
            label="Buscar Cliente",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True)
        )
            # Busqueda / cliente Masivo
        self.InptClienteMasiva = TextField(
            label="Buscar Cliente",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="black",italic=True)
        )

        # --- TABLA ---
            # --- Columnas de la tabla ---
        self.tablePru = DataTable(
            border= border.all(2,"purple"),
            border_radius=5,
            columns=[
                DataColumn(Text("ID_PRODUCTO",color="whithe",weight="bold")),
                DataColumn(Text("CLIENTE",color="whithe",weight="bold")),
                DataColumn(Text("PRODUCTO",color="whithe",weight="bold")),
                DataColumn(Text("FECHA",color="whithe",weight="bold")),
                DataColumn(Text("HERRAMIENTAS",color="whithe",weight="bold"))
            ],
        )
        self.showData() # Carga la función donde se recorre las tuplas de productos disponibles
  
    # -- Close Modal --
    def handle_close(self,e):
        self.page.close(self.dltButton)
        
    # -- Herramientas de la tabla --
    def dltButton(self,e):
        mdlDlt = AlertDialog(
            modal=True,
            title=Text("Alerta!"),
            content=Text(f"Estas Seguro de eliminar : {e.control.data[0]} ?"),
            actions=[
                TextButton("Eliminar",on_click=self.handle_close),
                TextButton("Cancelar",on_click=self.handle_close)
            ],
            actions_alignment= MainAxisAlignment.END
        )
        self.page.overlay.append(mdlDlt)
        mdlDlt.open = True
        self.update()


    # Muestra los datos de la base de datos
    def showData(self):
        self.tablePru.rows = []
        for row in self.dataTbl:    # Accede a la variable de la conexión
            self.tablePru.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text((row[0]))),
                        DataCell(Text(row[1])),
                        DataCell(Text(row[3])),
                        DataCell(Text(row[2])),
                        DataCell(
                            Row([
                                IconButton("delete",
                                    icon_color="red",
                                    data=row,
                                    on_click=self.dltButton # --- PROXIMA TAREA ---
                                ),
                                IconButton("edit",
                                    icon_color="green",
                                    data=row,
                                    #on_click=EditButton() # --- PROXIMA TAREA ---
                                )
                            ])
                        )
                    ]
                )
            )
        self.update()
        
    #-------------------------------------

    # --- CONTENEDORES,FRAMES ETC ... ---
        # Contenedor para el filtrado
        self.cntFiltPrinf = Container(
            expand=True,
            bgcolor="#222222",
            border_radius=5,
            padding=10,
            content= Row(
                controls=[
                    #Contenedor de busquedas masivas por ciente
                    Container(
                        expand=True,
                        bgcolor=self.color_teal,
                        border_radius=10,
                        padding=8,
                        content= Column(
                            controls=[  
                                Container(
                                    Text("Busqueda Masiva : ",color="whithe"),
                                    #self.InptPrindCard,
                                    alignment=alignment.center,
                                    bgcolor="black",
                                    border_radius=5
                                ),
                                self.InptClienteMasiva
                            ]
                        )
                    ),
                    # Contenedor de Busquedas Simples
                    Container(
                        expand=True,
                        bgcolor= self.color_teal,
                        border_radius=10,
                        padding=8,
                        alignment = alignment.center_right,
                        content= Column(
                            controls=[
                                Container( 
                                    Text("Buscar por : ",color="whithe"),
                                    #self.InptPrindCard,
                                    alignment=alignment.center,
                                    bgcolor="black",
                                    border_radius=5
                                ),
                                
                                self.InptPrindCard,
                                self.InptClienteSimple
                            ]
                        )
                    )
                ]
            ),
        )

        #Frame table
        self.cntTable = Container(
            bgcolor="#222222",  # Cambiado a azul para distinguir visualmente
            border_radius=10,
            alignment=alignment.top_center,
            expand=True,
            padding=10,
            content= Column( 
                expand=True,
                scroll="auto",
                controls=[
                    #self.data_table
                    ResponsiveRow(
                        controls=[
                            self.tablePru
                        ]
                    )
                   
                ]
            )
        )

        # Colocar los frames en forma de columna
        self.frameMain = Container(
            bgcolor="black",
            border_radius=10,
            padding=2,
            content=Column(
                    controls=[
                        self.cntFiltPrinf,
                        self.cntTable
                    ],
                ),
        )
        # Hacer responsiva los framaes en forma de Fila
        self.container = ResponsiveRow(
            controls=[
                self.frameMain
            ]
        )

    # IMPORTANTE : Retorna todos los Gidwts del promama
    def build(self):    
        return self.container

def main(page: Page):       #   page : Es el Frame o la ventana de la Aplicación
    page.window_min_height = 200
    page.window_min_width = 200
    page.theme_mode = ThemeMode.DARK
    page.padding = 5
    page.add(UI(page))

ft.app(main)
#pru()