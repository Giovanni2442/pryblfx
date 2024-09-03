from flet import * 
from src.pruebas.pru2 import FileUploaderApp
from src.views.VentanaCreate.createFicha.createPdf import CreatePdf
from src.Controllers.appPrindCard import appPrindCard


# Esta clase sirve como un Modulo Auxiliar para abrir y cerrar Modales
class Mdls():
    def __init__(self,page):

        self.page = page


        # IDENTIFICADOR DE INSERT Y UPDATE
        self.id = self.page.client_storage.get("id")
  
        
    def open_Cntndr(self,cnt):
        self.page.overlay.append(cnt)
        cnt.visible = True
        self.page.update()

    def Cls_Cntndr(self,cnt):
        #self.page.overlay.append(cnt)
        cnt.visible = False
        self.page.update()

        # Función para abrir el diálogo
    def open_dialog(self,dialog):
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    # Función para cerrar el diálogo
    def close_dialog(self,dialog):
        dialog.open = False
        self.page.update()
#'''
class opnMdlImg():
    def __init__(self,page):
        self.page = page
        # Abre y Cierra el modal
        self.mdl = Mdls(page)

        # PRU
        self.crdtPdf = CreatePdf(self.page)

        #EVENTO PICKER(PARA CARGAR ARCHIVOS)
        self.Img = FileUploaderApp(page)

    def open(self,id):
        self.mdlObsr = AlertDialog(     # Modal Observaciónes
            modal=True,
            title= Container(
                border=border.only(bottom=border.BorderSide(1, "#858585")),
                #border= border.only(bottom=border.BorderSide(1, "black")),
                shadow=BoxShadow(
                    spread_radius=0,
                    blur_radius=10,
                    offset=Offset(0, 4),  # Ajusta el desplazamiento de la sombra
                    color=colors.BLACK12,  # Cambia el color si es necesario
                ),
                content= Text(
                    "INGRESAR IMAGEN",
                    color="black",
                    text_align="center",
                ),
            ),
            
            bgcolor="#ddddddcf",  # Color de fondo con transparencia (CC es el valor alfa)
            content=
            Container(
                #bgcolor="#f0f0f0",
                width=500,
                height=250,
                margin=0,
                alignment=alignment.center,
                content=Column(
                    scroll="auto",          # Scroll
                    alignment=MainAxisAlignment.CENTER,  # Centra verticalmente el contenido dentro de la columna
                    horizontal_alignment=CrossAxisAlignment.CENTER,  # Centra horizontalmente el contenido dentro de la columna
                    controls=[
                        Text("Agregar Figura : ", color="black", text_align="center"),              # Agregar Imagem                       
                        ElevatedButton(
                            text="CARGAR!",
                            #color="RED",
                            bgcolor=colors.WHITE38,
                            color={
                                    ControlState.DEFAULT: colors.BLACK,
                                    ControlState.HOVERED: colors.RED,
                                },
                            on_click= self.Img.select_file # Función donde contiene el Picker
                        ),

                        Text("Ingresar Numero de Figura : ", color="black", text_align="center"),   # Agregar Num. Fig
                        TextField(
                            label="Figura",
                            border=InputBorder.OUTLINE,
                            border_color="Black",
                            height=100,
                            value="N/A",
                            color="black",
                            error_text="",
                            label_style=TextStyle(color="Black", italic=True),
                            #on_change= lambda e: self.valida.verInpts(e,filter.vrfPrintCard),
                            #on_change= lambda e: self.Img.select_file(e, e.control.value)
                        ),

                        Text("Ingresar Observaciónes", color="black", text_align="center"),
                        TextField(
                            label="Observaciónes",
                            border=InputBorder.OUTLINE,
                            border_color="Black",
                            multiline=True,
                            height=100,
                           value="N/A",         # <-- Hacer el Update para traer los datos sin borrarse
                            color="black",
                            error_text="",
                            label_style=TextStyle(color="black", italic=True),
                            #on_change= lambda e: self.valida.verInpts(e,filter.vrfPrintCard),
                            #on_change= lambda e: txt1 = e.control.value
                        )
                    ]
                ),
            ),
            actions=[
                Container(              # CONTENEDOR DE BOTONES
                    content=Row(
                        vertical_alignment=CrossAxisAlignment.END,
                        controls=[
                        # ABRIR MODAL
                        FilledButton("AGREGAR",  # AGREGAR CAMBIOS
                            adaptive=True,
                            style=ButtonStyle(
                                bgcolor=colors.WHITE54,
                                color={
                                    ControlState.HOVERED: colors.WHITE,
                                    ControlState.DEFAULT: colors.BLACK,
                                },
                                overlay_color=colors.RED_800,
                                #overlay_color=colors.TRANSPARENT,
                                elevation={"pressed": 0, "": 1},
                                animation_duration=300,
                                shape={
                                    ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                                    ControlState.DEFAULT: RoundedRectangleBorder(radius=3),
                                },
                            ),
                            # TAREA : CONFIRMA LOS CAMBIOS Y CIERRA EL MODAL, AGREGAR UN MENSAJE DE CONFIRMACIÓN!
                            on_click= lambda _: self.Img.jer(id,self.mdlObsr.content.content.controls[3].value,self.mdlObsr.content.content.controls[5].value)
                            #on_click= lambda _: self.crdtPdf.jir(id,self.mdlObsr.content.content.controls[3].value,self.mdlObsr.content.content.controls[5].value)
                        ),
                        # CERRAR MODAL
                        FilledButton("CERRAR",  # CERRAR MODAL
                            adaptive=True,
                            style=ButtonStyle(
                                bgcolor=colors.WHITE54,
                                color={
                                    ControlState.HOVERED: colors.WHITE,
                                    ControlState.DEFAULT: colors.BLACK,
                                },
                                overlay_color=colors.RED_800,
                                #overlay_color=colors.TRANSPARENT,
                                elevation={"pressed": 0, "": 1},
                                animation_duration=300,
                                
                                shape={
                                    ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                                    ControlState.DEFAULT: RoundedRectangleBorder(radius=3),
                                },
                            ),
                            on_click=lambda e: self.mdl.close_dialog(self.mdlObsr)
                        )
                    ])
                ),
                ]
            )
        print("---> ",self.mdlObsr.content.content.controls[3].value)       # TextField Num.Fig
        print("---> ",self.mdlObsr.content.content.controls[5].value)       # TextField Observaciones
        print("---> ",self.mdlObsr.content.content.controls[1])       # TextField Observaciones

        self.mdl.open_dialog(self.mdlObsr)#'''

    def dataPdf(self,default_value,Indx):
        if self.id != "Insert":   
            return self.id
            return f"{Indx}"
        else:
            return default_value
        
    # OBTIENE DATOS POR MEDIO DE SU ID
    def tplInpts(self):
        return [
            self.id_product,
            self.cliente,
            self.fecha_Elav,
            self.fecha_Rev,
            self.producto
        ]
            