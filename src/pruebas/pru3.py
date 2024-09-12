import flet as ft


def main(page):
  def checkbox_changed(e):
    t.value = f"Checkbox value changed to {c.value}" 
    t.update()

  c = ft.Checkbox(label="Checkbox with 'change' event", on_change=checkbox_changed)
  t = ft.Text()

  page.add(c, t)

ft.app(main)