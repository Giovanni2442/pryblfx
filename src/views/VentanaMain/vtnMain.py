import flet as ft
from flet import *

import flet as ft

class MyApp(UserControl):
    def __init__(self, page):
        self.page = page
        self.setup_ui()

    def setup_ui(self):
        self.t = ft.Text()
        self.tb = ft.TextField(
            label="Textbox with 'change' event:",
            on_change=self.textbox_changed,
        )
        self.page.add(self.tb, self.t)

    def textbox_changed(self, e):
        self.tb.value = e.control.value
        print(self.tb.value)
        self.page.update()

def main(page: ft.Page):
    app = MyApp(page)

ft.app(target=main)
