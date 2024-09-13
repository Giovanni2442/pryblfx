#'''##--Draw and drop--##
from flet import * 

from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

class FileUploaderApp:
    def __init__(self, page: Page):
        self.page = page
        self.file_picker = FilePicker(on_result=self.on_file_picked)        # Abre el administrador de busqueda de Windows
        self.page.overlay.append(self.file_picker) 
        
        self.crtPdf = CreatePdf(self.page)                         # Agregar el picker a la aplicación 
    
        self.pru = "N/A"        # <- PROBAR CON None ó N/A
        # Id button
        self.Btnid = None
        #Lista de imagenes
        self.tplImg={}              # Guarda las rutas de las imagenes Ingresadas y Las observaciónes

    def on_file_picked(self, e: FilePickerResultEvent):                     # Si existe un archivo, muestra los multiples archivos
        if e.files:     
            for file in e.files:    # Recorre la lista de la info. de la imagen
                self.pru = file.path

    def select_file(self, e):       # Función para agregar multiples archivos
        # ALmacena el Id del bton
        #print(any)
        self.file_picker.pick_files(allow_multiple=False)

    def jer(self,*any):     # Inserción al PDF y a la base de datos (PROXIMAMENTE!)
        #self.crtPdf.jir1(any)
        self.Btnid = any
        id = self.Btnid[0]
        numFig = self.Btnid[1]
        Obsrv = self.Btnid[2]
        #self.crtPdf.InsertTxt()
        self.tplImg[self.Btnid[0]] = (self.pru,numFig,Obsrv)        # DICCIONARIO DONDE ALMACENA CADA BTN INGRESADO!
        self.pru = "N/A"
        print("tpl -- ",self.tplImg)
        self.page.client_storage.set("id_Img",self.tplImg)           # <-- DICCIONARIO ACCECIBLE
       

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

#app(target=main)'''

    

