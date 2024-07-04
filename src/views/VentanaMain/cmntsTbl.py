from flet import *
from src.Controllers.appTable import Controllers
#from src.views.VentanaMain.pruebasFlet2 import UI

class cntTable(UserControl):
    def __init__(self,page):
        super().__init__()

        self.page = page
        self.dataTbl = Controllers()  #Accede a la información en la base de datos
        
        # --- TABLA ---
            # --- Columnas de la tabla ---
        self.Table = DataTable(
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
        # row table
        self.showData() # Carga la función donde se recorre las tuplas de productos disponibles

    # -- Herramientas de la tabla --
        # --- Delete Product ---
    def dltButton(self,e):
        idPrind = e.control.data[0]
        self.mdlDlt = AlertDialog(
            modal=True,
            title=Text("Alerta!"),
            content=Text(f"Estas Seguro de eliminar : {idPrind} ?"),
            actions=[
                #TextButton("Eliminar",on_click= lambda _: self.btnSlct(bnd=True,id=idPrind)),   # lambda _ : "_" el guión sirve para tomar ignorar los parametros, ya que no se usan en la función  
                TextButton("Eliminar",on_click= lambda _: self.btnSlct(bnd=True,id=idPrind)),
                TextButton("Cancelar",on_click= lambda _: self.btnSlct(bnd=False,id=None))
            ],
            actions_alignment= MainAxisAlignment.END
        )
        self.page.overlay.append(self.mdlDlt)
        self.mdlDlt.open = True
        self.page.update()
        # --------------

    # --  Modal Delete --
    def btnSlct(self,bnd,id):
        if not bnd:
            self.mdlDlt.open = False
        else:
            self.dataTbl.delete_row_Table(id=id)
            self.mdlDlt.open = False
            # -- Limpia y Actualiza la tabla -- 
            self.Table.rows.clear() 
            self.showData()
            self.page.update()
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
            self.update()
        self.page.update()
        
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
                            #on_click=EditButton() # --- PROXIMA TAREA ---
                        )
                    ])
                )
            ]
        )
        return self.rows

    # Muestra los datos de la base de datos
    def showData(self):
        self.Table.rows = []
        for row in self.dataTbl.get_row_Table():    # Accede a la variable de la conexión
            self.Table.rows.append(
               # self.dataRows(row)
               self.dataRows(row)
            )
            self.update()

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
                    ResponsiveRow(
                        controls=[
                            self.Table
                        ]
                    )
                ]
            )
        )
        
    def build(self):
        return super().build()