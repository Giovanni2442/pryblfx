##--Draw and drop--##
from flet import * 

from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

#SI AL TENER MULTIPLES UPLOADFILE, QUIERO ALMACENAR
# EN UNA LISTA PARA PASARLA COMO IMAGENES Y AGREGAR EL INDICE QUE CORRECPONDA 
# ACADA OBSERVACIÓN


#TAREAS#
#Al implementar la imagen y descripci+ón, esto imprimaria crear
#Una nueva tabla para ello
class FileUploaderApp:
    def __init__(self, page: Page):
        self.page = page
        self.file_picker = FilePicker(on_result=self.on_file_picked)        # Abre el administrador de busqueda de Windows
        self.page.overlay.append(self.file_picker) 
        
        self.Img = CreatePdf()                         # Agregar el picker a la aplicación 
        #Liata de imagenes
        self.tplImg=[]

    def on_file_picked(self, e: FilePickerResultEvent):                     # Si existe un archivo, muestra los multiples archivos
        if e.files:     
            for file in e.files:    # Recorre la lista de la info. de la imagen
                #self.Img.Insert(file.path)
                #self.Imge.Insert(file.path)
                self.tplImg.append(file.path)
                print(self.tplImg)
                #self.page.add( Text(f"Archivo seleccionado: {file.name}"))

    def select_file(self, e):       # Función para agregar multiples archivos
        self.file_picker.pick_files(allow_multiple=False)

    def build(self):
        return Column(
            [
                Text("Subir archivo usando Flet"),
                ElevatedButton(
                    "Seleccionar archivo",
                    on_click=self.select_file,
                ),
            ]
        )

#def main(page: Page):
#    app = FileUploaderApp(page)
#    page.add(app.build())

#app(target=main)

    

