import flet as ft
import sqlite3
import fitz  # PyMuPDF
import io

from src.Controllers.appPrindCard import appPrindCard
resultado = appPrindCard()

def abrir_pdf(nombre_archivo):
    pdf_path = resultado.getPridCardPdf(nombre_archivo)
    
    if pdf_path:
        # Decodificar la ruta del PDF de bytes a string
        ruta_pdf = pdf_path[0].decode('utf-8')
        print(f"Ruta del PDF: {ruta_pdf}")  # Para depuración
        
        return ruta_pdf  # Devolver la ruta del PDF
    else:
        print(f"No se encontró el PDF con nombre '{nombre_archivo}'.")
        return None

def on_button_click(e, page):
    nombre_archivo = text_field.value
    if nombre_archivo:
        pdf_path = abrir_pdf(nombre_archivo)
        if pdf_path:
            # Crear un botón de descarga
            page.add(ft.Image(src=f"file://{pdf_path}"))  # Muestra una vista previa del PDF
            page.add(ft.CupertinoFilledButton(url=f"file://{pdf_path}", label="Descargar PDF"))
    else:
        print("Por favor, introduce un nombre de archivo.")

def main(page: ft.Page):
    global text_field

    # Crear un campo de texto para ingresar el nombre del archivo PDF
    text_field = ft.TextField(label="Nombre del archivo PDF")

    # Crear un botón para buscar y abrir el PDF
    button = ft.CupertinoFilledButton(text="Abrir PDF", on_click=lambda e: on_button_click(e, page))

    # Agregar los componentes a la página
    page.add(text_field, button)

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main)


