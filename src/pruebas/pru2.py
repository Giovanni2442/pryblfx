import flet as ft
import sqlite3
import webbrowser
import fitz  # PyMuPDF
import os

from src.Controllers.appPrindCard import appPrindCard
resultado = appPrindCard()

def main(page: ft.Page):
    def open_pdf(e):
        # Recuperar el archivo PDF de la base de datos
        pdf_data = resultado.getPridCardPdf("121212")[0]  # Supongamos que queremos el PDF con ID 1
        if pdf_data:
            # Guardar temporalmente el PDF en el disco
            with open("Template/archivo_temporal.pdf", "wb") as file:
                file.write(pdf_data)

            ruta = "Template/archivo_temporal.pdf"

            if os.path.exists(ruta):
                webbrowser.open(f'file://{os.path.abspath(ruta)}')
            else:
                print("El archivo no existe.")
            
            #webbrowser.open(f'Template/archivo_temporal.pdf')
            # Abrir el archivo PDF
            #page.launch_url("C:/Users/gumrt/Desktop/pryblfx/venv/src/FichasTecnicas/D-0392_R-2.pdf")

    button = ft.ElevatedButton("Abrir PDF", on_click=open_pdf)
    page.add(button)

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main)

