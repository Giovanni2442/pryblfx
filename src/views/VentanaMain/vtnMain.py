import flet as ft
def main(page: ft.Page):

    def validate_input(e):
        if not input_field.value.isdigit():
            input_field.error_text = "Por favor, ingrese solo números."
        else:
            input_field.error_text = ""
        page.update()

    input_field = ft.TextField(
        label="Ingrese un número",
        on_change=validate_input
    )

    page.add(input_field)

# Ejecutar la aplicación
ft.app(target=main)
