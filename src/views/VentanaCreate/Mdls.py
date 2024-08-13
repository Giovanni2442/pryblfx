from flet import * 
from src.pruebas.pru2 import FileUploaderApp

# Esta clase sirve como un Modulo Auxiliar para abrir y cerrar Modales
class Mdls():
    def __init__(self,page):
        self.page = page
        

        # Función para abrir el diálogo
    def open_dialog(self,dialog):
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
    # Función para cerrar el diálogo
    def close_dialog(self,dialog):
        dialog.open = False
        self.page.update()

class opnMdlImg():
    def __init__(self,page):
        self.page = page
        # Abre y Cierra el modal
        self.mdl = Mdls(page)

        #EVENTO PICKER(PARA CARGAR ARCHIVOS)
        self.Img = FileUploaderApp(page)

    def open(self, e, id):
        self.mdlObsr = AlertDialog(
            modal=True,
            title=Text(
                "IMAGEN",
                color="black",
                text_align="center"
                ),
            bgcolor="#ddddddcf",  # Color de fondo con transparencia (CC es el valor alfa)
            content=Container(
                bgcolor="#f0f0f0",
                width=500,
                height=250,
                margin=0,
                alignment=alignment.center,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,  # Centra verticalmente el contenido dentro de la columna
                    horizontal_alignment=CrossAxisAlignment.CENTER,  # Centra horizontalmente el contenido dentro de la columna
                    controls=[
                        ElevatedButton(
                            text="UPLOAD!",
                            on_click=lambda e: self.Img.select_file(e, id)  # Función donde contiene el Picker
                        ),
                        TextField(
                            label="Dinaje",
                            border=InputBorder.OUTLINE,
                            border_color="Black",
                            multiline=True,
                            height=100,
                            value="N/A",
                            error_text="",
                            label_style=TextStyle(color="Black", italic=True),
                            # on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
                        )
                    ]
                ),
            ),
            actions=[
                TextButton("CERRAR", on_click=lambda e: self.mdl.close_dialog(self.mdlObsr))
                ]
            )
        self.mdl.open_dialog(self.mdlObsr)

            