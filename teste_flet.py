import flet as ft

def main(pagina):
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)
    
    botao = ft.ElevatedButton("Iniciar char")
    pagina.add(botao)


ft.app(main)