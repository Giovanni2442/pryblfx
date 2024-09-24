import base64
import io
import flet as ft
import fitz
import webbrowser
import os
from flet import * 
from src.Controllers.appPrindCard import appPrindCard
#from src.views.VentanaCreate.createFicha.createPdf import CreatePdf
from src.views.VentanaCreate.Mdls import Mdls

class opnPrindPdf():
    def __init__(self,page):
        super().__init__()

        #pass
    #'''
        # Instancia hacia los qury's para el PDF
        self.qryPrndCrd = appPrindCard
        self.page = page

        #Abrir y Cerrar Modales
        self.mdl = Mdls(page)

        #self.crtPdf = CreatePdf #'''

    def opnPdfBffer(self,e):
        #pass
        #'''
        idPrind = e.control.data[0]                                 # OBTENER EL ID DESDE EL EVENTO ON_CLICK
        getPdf = self.qryPrndCrd().getPridCardPdf(idPrind)[0]       # OBTIENEN EL BINARIO DEL PDF PARA CONVERTIRLO
        
        #print(getPdf)

        # Recuperar el archivo PDF de la base de datos
        if getPdf:

            try:
                # Crear un buffer en memoria para el PDF
                pdf_buffer = io.BytesIO(getPdf)

                # Abrir el PDF desde el buffer
                pdf_document = fitz.open("pdf", pdf_buffer)

                temp_pdf_path = "Template/archivo_temporal.pdf"
                pdf_document.save(temp_pdf_path)
            except Exception as e:
                #print("CIERRA EL ARCHIVO!")
                self.mdlClsPdf = AlertDialog(   # MODAL PRODUCTO DUPLICADO
                        modal=True,
                        title= Text(f"PrindCard Abierto!"),
                        actions=[
                            TextButton("CERRAR", on_click=lambda e: self.mdl.close_dialog(self.mdlClsPdf))
                        ]
                    )
                    #self.msgDlt(self.mdlDplctPrdct)
                self.mdl.open_dialog(self.mdlClsPdf)
            finally:
                pdf_document.close()  # Cerrar el documento
            
            if os.path.exists(temp_pdf_path):
                webbrowser.open(f'file://{os.path.abspath(temp_pdf_path)}')
            else:
                print("El archivo no existe.")

        self.page.update()#'''

    def openPdfLocal(self,e):
        idPrind = e.control.data[0]                                     # OBTENER EL ID DESDE EL EVENTO ON_CLICK
        getPdf = self.qryPrndCrd().getPridCardPdfLOCAL(idPrind)[0]      # OBTIENE LA RUTA DEL PDF, regresa una tupla
        #print("id : ", idPrind)
        print(getPdf)
       # '''
        # Comprobar si se ha recuperado una ruta válida
        if getPdf:
            try:
                # Comprobar si el archivo existe en la ruta obtenida
                if os.path.exists(getPdf):
                    webbrowser.open(f'file://{os.path.abspath(getPdf)}')
                else:
                    #print("El archivo no existe.")
                    self.mdlClsPdf = AlertDialog(   # MODAL PRODUCTO DUPLICADO
                            modal=True,
                            title=Text(f"Archivo no encontrado!"),
                            actions=[
                                TextButton("CERRAR", on_click=lambda e: self.mdl.close_dialog(self.mdlClsPdf))
                            ]
                        )
                    self.mdl.open_dialog(self.mdlClsPdf)

            except Exception as e:
                #print("Error al abrir el archivo:", e)
                self.mdlClsPdf = AlertDialog(   # MODAL PRODUCTO DUPLICADO
                        modal=True,
                        title= Text(f"Error al abrir el archivo!"),
                        actions=[
                            TextButton("CERRAR", on_click=lambda e: self.mdl.close_dialog(self.mdlClsPdf))
                        ]
                    )
                self.mdl.open_dialog(self.mdlClsPdf)

        self.page.update()#'''


            