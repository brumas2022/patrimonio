#import streamlit as st
class Calculo:
    def __init__(self, altura, largura, comprimento, diametro, velocidade):
        self.altura = altura
        self.velocidade = velocidade
        self.largura = largura
        self.comprimento = comprimento
        self.diametro = diametro
    def quadrado(self):
        return int(largura*comprimento)
    def chutar(self):
        print("Mirar")
        print("Encostar na bola com 2x a força de passe do jogador")


metro = Calculo(10,20,30,40,50)

resposta = metro.quadrado
print (resposta)
