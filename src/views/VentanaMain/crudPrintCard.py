import os
from typing import Any, List
import flet as ft
from flet import *          # Se importa todos los componentes de la Libreria "flet"
from src.Controllers.appdb import appDb
from src.Controllers.appFichVent import appFichVent
from src.views.VentanaCreate.createPrindCard import createPrind
from src.views.VentanaMain.vtnMain import pr
from src.views.VentanaMain.openPdf.opnPrindPdf import opnPrindPdf

class crudPrintCard(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame
        self.color_teal = "teal"
        #'''
    # ########## COMPONENTES ############################
        self.page = page  

        self.dataTbl = appFichVent  #Accede a la información en la base de datos
    
        # path ruta local#
        self.pdf_path = ""
        # PATH RUTA LOCAL IMAGENES
        self.ImgPdf = ""

        #self.createPrnt = createPrind(page)
        self.pr = pr(page)
        self.pdf = opnPrindPdf(page)#'''

        # --- INPUTS DE BUSQUEDA --- 
            # Busqueda del PrindCard
        self.InptPrindCard = TextField(
            label="Buscar PridCard",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e : self.searchInput(e,i=0)
        )
            # Busqueda por cliente
        self.InptClienteSimple = TextField(
            label="Buscar Cliente",
            suffix_icon= icons.SEARCH,
            border= InputBorder.UNDERLINE,
            border_color= "black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e : self.searchInput(e,i=1)
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
            on_click= lambda _: (
                page.client_storage.set("id", "Insert"),
                self.page.go('/cratePrindCard'),
            ),
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
            on_click= lambda _: self.page.go('/editMsv'),
        )

        # --- TABLA ---
            # --- Columnas de la tabla ---
        self.Table = DataTable(
            #border= border.all(2,"purple"),
            #border_radius=2,
            expand=True,
            bgcolor="#146364",
            data_row_color = colors.WHITE70,
            border_radius=border_radius.only(top_left=10,top_right=10),
            vertical_lines= BorderSide(0.5,color=colors.WHITE24),
            columns=[
                DataColumn(Text("ID_PRODUCTO",color=colors.WHITE,weight="bold")),
                DataColumn(Text("CLIENTE",color=colors.WHITE,weight="bold")),
                DataColumn(Text("PRODUCTO",color=colors.WHITE,weight="bold")),
                DataColumn(Text("FECHA",color=colors.WHITE,weight="bold")),
                DataColumn(Text("HERRAMIENTAS",color=colors.WHITE,weight="bold"))
            ],
        )
        # row table
        self.showData() # Carga la función donde se recorre las tuplas de productos disponibles

    # -- Herramientas de la tabla --
        # --- Delete Product ---
        # Modularizar el Modal para Eliminar, Atualizar y Agregar
    def dltButton(self,e):
        idPrind = e.control.data[0]
        print(e.control.data)
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
    
        # -- Query Modal Delete --
    
    # ELIMINA LOS PDF Y SUS IMAGENES
    def dltPdfImgs(self,id):
        # LISTA DE RUTAS DE IMAGENES Y PDF
        urlPdf = [
            # ELIMINAR PDF DESDE LA RUTA LOCAL}
            f'FilePdf/{id}.pdf',
            # ELIMINAR  IMAGENES DEL PDF
            f'Imagenes/EXTRC/{id}.png',
            f'Imagenes/IMPRC/{id}.png',
            f'Imagenes/LMNSN/{id}.png',
            f'Imagenes/RFLD/{id}.png',
            f'Imagenes/CNVRSN/{id}.png',
        ]

        for url in urlPdf:
            try:
                os.remove(url)
                print(f"Archivo eliminado: {url}")
            except FileNotFoundError:
                pass
                #print(f'Archivo o imagen {url} No encontrado!')

    # ELIMINA LOS REGISTROS DE LA BASE DE DATOS
    def queryDlt(self,bnd,id):
        if not bnd:
            self.mdlDlt.open = False
        else:
            # ELIMINA DATOS DEL PRINDCARD#
            self.dataTbl().delete_row_Table(id)
            # ELIMINA REGISTRO DEL PDF#
            self.dltPdfImgs(id)
        
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
            #color="yellow",
            cells=[
                DataCell(Text(row[0],color=colors.BLACK,theme_style=TextThemeStyle.BODY_LARGE,font_family="Arial")),
                DataCell(Text(row[1],color=colors.BLACK,theme_style=TextThemeStyle.BODY_LARGE,font_family="Arial")),
                DataCell(Text(row[3],color=colors.BLACK,theme_style=TextThemeStyle.BODY_LARGE,font_family="Arial")),
                DataCell(Text(row[2],color=colors.BLACK,theme_style=TextThemeStyle.BODY_LARGE,font_family="Arial")),
                DataCell(
                    Row([
                        IconButton("delete",
                            #icons.CHECK,
                            icon_color=colors.BLACK54,
                            data=row,
                            on_click=self.dltButton # --- PROXIMA TAREA ---
                        ),
                        IconButton("edit",
                            icon_color=colors.BLACK54,
                            data=row,
                            on_click= lambda e: (
                                self.page.client_storage.set("id",e.control.data[0]),
                                self.page.go('/cratePrindCard'),
                            ),
                        ),
                        IconButton("NEWSPAPER", # Ficha Tecnica
                            icon_color=colors.BLACK54,
                            data=row,
                            on_click= self.pdf.openPdfLocal     # ABRE EN LOCAL
                            #on_click= self.pdf.opnPdfBffer     # ABRE EN BD
                        )
                    ])
                )
            ]
        )
        return self.rows
    
    # --- BUSCADORES ---
        # inpt  : Input que se va a utilizar
        # e     : Evento de escucha
        # i     : El atributo de la tabla donde buscara i = 0 : id_pridcard ; i = 1 : cliente
    def searchInput(self,e,i):
        srchInpt = e.control.value.lower()  # Convierte a minuscula la enrada de Texto
        #print( e.control.value.lower())
        filterId = list(filter(lambda x: srchInpt in x[i].lower(), self.dataTbl().get_row_Table()))       # Toma la tabla padre FichaTecnica
        #print("you find : ",filterId)
        self.Table.rows = []

        # Si el input es diferente de vacio
        if not e.control.value == "":
            # Si la list que se creo es mayor a cero, significa que encontro coincidencias
            print(len(filterId))
            if len(filterId) > 0:
                #self.dataNotFound = False
                for row in filterId:
                    self.Table.rows.append(             # Agregar a la Tabla las coincidencias de la busqueda
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
        
    #''' <-- DESCOMENTAR -->
    # Muestra los datos de la base de datos
    def showData(self):
        #'''
        self.Table.rows = []
        for row in self.dataTbl().get_row_Table():    # Accede a la variable de la conexión
            self.Table.rows.append(
                self.dataRows(row)
            )
        self.update()#'''
        #pass
        
    #######################################################

    # --- CONTENEDORES,FRAMES ETC ... ---
        # --- FRAME FILTRADO ---
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
                                    Text("FICHA TECNICA",color=colors.BLACK38,theme_style=TextThemeStyle.TITLE_SMALL),
                                    border=border.only(bottom=border.BorderSide(0.5, colors.BLACK87)),
                                    #expand=True,
                                    #self.InptPrindCard,
                                    alignment=alignment.center,
                                    height=50,
                                    #bgcolor=colors.AMBER,
                                    border_radius=0
                                ),
                                
                                self.InptPrindCard,
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
            bgcolor= colors.WHITE54,  # Cambiado a azul para distinguir visualmente
            border_radius=5,
            alignment=alignment.top_center,
            expand=True,
            padding=5,
            margin= margin.only(left=0,right=0,top=-5,bottom=0),
            content= Column( 
                expand=True,
                scroll="auto",
                controls=[
                    Row(
                        #scroll="auto",                     
                        controls=[
                            self.Table
                        ]
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
'''
def main(page: Page):       #   page : Es el Frame o la ventana de la Aplicación
    page.window_min_height = 200
    page.window_min_width = 200

    #page.theme_mode = ThemeMode.DARK
    page.padding = 0
    #page.adaptive = True
    page.add(crudPrintCard(page))


app(main)
#pru()'''