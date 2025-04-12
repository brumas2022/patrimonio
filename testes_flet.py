import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()
    page.title = "Meu primeiro teste com Flet"
    t = ft.Text(value="Vamos mudar o mundo", color="green")
    page.controls.append(t)
    page.update()
    new_task = ft.TextField(hint_text="O que vamos fazer agora", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
ft.app(main)