from typing import Any, List
import flet as ft
from flet import *          # Se importa todos los componentes de la Libreria "flet"
from src.Controllers.appTable import Controllers
from src.Controllers.appCreatePrindCard import CntrlsCreatePrindCard
from src.views.VentanaCreate.createPrindCard import createPrind
from src.views.VentanaMain.vtnMain import pr


#  --- TASK --- 
# * Conectar todas las tablas a la base de datos (Hacer el intento de forma abstracta)
# * Empezar a hacer un prototipo de insersión al pdf 
# * Conectar sus respectivas verificaciónes

def pru():
    db = Controllers().get_row_Table()
    print(db)
    #pass

class crudPrintCard(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

    # ########## COMPONENTES ############################
        self.page = page  
        self.color_teal = "teal"
        #self.inptTable = InptsTable(page)
        self.dataTbl = Controllers()  #Accede a la información en la base de datos
        self.InsrtData = CntrlsCreatePrindCard()

        self.createPrnt = createPrind(page)
        self.pr = pr(page)
        # --- INPUTS DE BUSQUEDA --- 
            # Busqueda del PrindCard
        self.InptPrindCard = TextField(
            label="Buscar PridCard",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True),
            on_change=self.searchInput
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
  
        # --- BOTONES ---
            ###  - CREAR UN NUEVO PRIND CARD  - ###

        self.BtnCreate = FilledButton(
            text="Crear PrindCard",
            adaptive=True,
            style=ButtonStyle(
                bgcolor="#21A772",
                color={
                    ControlState.HOVERED: colors.RED,
                    ControlState.HOVERED: colors.BLACK,
                },
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=200,
                shape={
                    ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                    ControlState.DEFAULT: RoundedRectangleBorder(radius=3),
                },
            ),
            #on_click= lambda _: self.page.go('/cratePrindCard'),
            #on_click= self.inptTable.jer
        )

        self.BtnCreate2 = FilledButton(
            text="Crear PrindCard 2",
            adaptive=True,
            style=ButtonStyle(
                bgcolor="#21A742",
                color={
                    ControlState.HOVERED: colors.RED,
                    ControlState.HOVERED: colors.BLACK,
                },
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=200,
                shape={
                    ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                    ControlState.DEFAULT: RoundedRectangleBorder(radius=3),
                },
            ),
            on_click= lambda _: self.page.go('/cratePrindCard'),
            #on_click= self.btnInsert
        )

        # --- TABLA ---
            # --- Columnas de la tabla ---
        self.Table = DataTable(
            border= border.all(2,"purple"),
            border_radius=5,
            vertical_lines= BorderSide(1,"whithe"),
            columns=[
                DataColumn(Text("ID_PRODUCTO",color="whithe",weight="bold")),
                DataColumn(Text("CLIENTE",color="whithe",weight="bold")),
                DataColumn(Text("PRODUCTO",color="whithe",weight="bold")),
                DataColumn(Text("FECHA",color="whithe",weight="bold")),
                DataColumn(Text("HERRAMIENTAS",color="whithe",weight="bold"))
            ],
        )
        # row table
        self.showData() # Carga la función donde se recorre las tuplas de productos disponibles

    # -- Herramientas de la tabla --
        # --- Delete Product ---
        # Modularizar el Modal para Eliminar, Atualizar y Agregar
    def dltButton(self,e):
        idPrind = e.control.data[0]
        self.mdlDlt = AlertDialog(
            modal=True,
            title=Text("Alerta!"),
            content=Text(f"Estas Seguro de eliminar : {idPrind} ?"),
            actions=[
                #TextButton("Eliminar",on_click= lambda _: self.btnSlct(bnd=True,id=idPrind)),   # lambda _ : "_" el guión sirve para tomar ignorar los parametros, ya que no se usan en la función  
                TextButton("Eliminar",on_click= lambda _: self.queryDlt(bnd=True,id=idPrind)),
                TextButton("Cancelar",on_click= lambda _: self.queryDlt(bnd=False,id=None))
            ],
            actions_alignment= MainAxisAlignment.END
        )
        self.page.overlay.append(self.mdlDlt)
        self.mdlDlt.open = True
        self.page.update()
        # ----

        ##### QUERYS ########
        # -- Query Update
    def updateButton(self,e):
        self.page.go('/prueba')
        self.pr.update(e.control.data[0])
        self.pr.qt = e.control.data[0]
        
        # -- Query Modal Delete --
    def queryDlt(self,bnd,id):
        if not bnd:
            self.mdlDlt.open = False
        else:
            self.dataTbl.delete_row_Table(id=id) 
            self.mdlDlt.open = False
            # -- Limpia y Actualiza la tabla -- 
            self.Table.rows.clear() 
            self.showData()
            # Mensaje parte inferior
            self.msgDlt = SnackBar(
                content=Column(
                    controls=[
                        Container(
                            Text(f"Se elimino : {id}",size=20,color="white"),
                            alignment=alignment.center
                        ),
                    ],
                ),
                bgcolor="#831D1D",
            )
            self.page.overlay.append(self.msgDlt)
            self.msgDlt.open = True 
        self.page.update()
        
        # -----------------------------

     # --- Filas de la tabla ---
    def dataRows(self,row):
        self.rows = DataRow(
            cells=[
                DataCell(Text((row[0]))),
                DataCell(Text(row[1])),
                DataCell(Text(row[3])),
                DataCell(Text(row[2])),
                DataCell(
                    Row([
                        IconButton("delete",
                            #icons.CHECK,
                            icon_color="red",
                            data=row,
                            on_click=self.dltButton # --- PROXIMA TAREA ---
                        ),
                        IconButton("edit",
                            icon_color="green",
                            data=row,
                            on_click= self.updateButton # --- PROXIMA TAREA ---
                        )
                    ])
                )
            ]
        )
        return self.rows
    
    # --- BUSCADORES ---
        # inpt  : Input que se va a utilizar
        # e     : Evento de escucha
    def searchInput(self,e):
        srchInpt = e.control.value.lower()
        print(srchInpt)
        filterId = list(filter(lambda x: srchInpt in x[0].lower(), self.dataTbl.get_row_Table()))
        print("you find : ",filterId)
        self.Table.rows = []

        # Si el input es diferente de vacio
        if not e.control.value == "":
            # Si la list que se creo es mayor a cero, significa que encontro coincidencias
            print(len(filterId))
            if len(filterId) > 0:
                #self.dataNotFound = False
                for row in filterId:
                    self.Table.rows.append(
                        self.dataRows(row),
                    )
                self.update()
            else:
                print("data no found!")
                self.dataRows("data not fount")
                self.update()
        # Si no hay datos en el TextFile Vuelve a mostrar los datos en la tabla
        else:
            self.showData(),
            self.update()
                
        # Componenete de Dato No Encontrado! para el Buscador de la tabla       
        self.dataNotFound = Text("No se encontro el Producto!",
                weight="bold",
                size=20
            )

    # Muestra los datos de la base de datos
    def showData(self):
        self.Table.rows = []
        for row in self.dataTbl.get_row_Table():    # Accede a la variable de la conexión
            self.Table.rows.append(
                self.dataRows(row)
            )
        self.update()
        
    #######################################################

    # --- CONTENEDORES,FRAMES ETC ... ---
        # --- FRAME FILTRADO ---
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
                                self.InptClienteSimple,
                                # Se coloca en un contenedor para centar
                                Container(
                                    expand=True,
                                    alignment=alignment.bottom_right,
                                    #bgcolor="yellow",
                                    padding=5,
                                    border_radius=3,
                                    content= Row(
                                        controls= [
                                            self.BtnCreate,
                                            self.BtnCreate2
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            ),
        )

        # --- FRAME TABLE ---
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
                    Container(
                        #expand=True,
                        bgcolor="red",
                        margin=0,
                        border_radius=3,
                        alignment=ft.alignment.center,
                        content=Text("Lista de PrindCards"),
                    ),
                    ResponsiveRow(                        
                        controls=[
                            self.Table
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
    page.add(crudPrintCard(page))


#app(main)
#pru()'''