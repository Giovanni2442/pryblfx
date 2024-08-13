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
        
        # Id button
        self.Btnid = None
        #Liata de imagenes
        self.tplImg={}              # Guarda las rutas de las imagenes Ingresadas y Las observaciónes

    def on_file_picked(self, e: FilePickerResultEvent):                     # Si existe un archivo, muestra los multiples archivos
        #numFig = self.Btnid[1]
        #Obsrv = self.Btnid[2]
        
        if e.files:     
            for file in e.files:    # Recorre la lista de la info. de la imagen
            
                #if len(self.Btnid)
                #if self.Btnid[0] == "1" : #Banderin confirma si se precióno el boton
                #   self.tplImg[self.Btnid[1]] = (file.path,) 
                #self.Img.Insert(self.tplImg) 
                #print("-- ",self.tplImg)
                print(file)
                #print(f"NumFig : {numFig} : Obsrv : {Obsrv}")
                #self.page.add( Text(f"Archivo seleccionado: {file.name}"))

    def select_file(self, e, *any):       # Función para agregar multiples archivos
        # ALmacena el Id del bton
        self.Btnid = self
        #print(any)
        self.file_picker.pick_files(allow_multiple=False)

        #self.on_file_picked(e,label)
    
    def jer(self,e,*any):
        return any

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

    

