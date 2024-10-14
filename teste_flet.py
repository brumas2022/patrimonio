import flet as ft

def main(pagina):
    titulo = ft.Text("Historico escolar")
    pagina.add(titulo)
    
    
    botao = ft.ElevatedButton("Primeiro Grau")
    botao1 = ft.ElevatedButton("Segundo Grau")
    botao3 = ft.ElevatedButton("Terceiro Grau")
    
    pagina.add(botao)
    pagina.add(botao1)
    pagina.add(botao3)


ft.app(main)