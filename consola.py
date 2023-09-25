from typing import Optional

from asistente import Asistente

class UIconsola:
    def __init__(self):
        self.asistente: Asistente = Asistente()


    @staticmethod
    def menu():
        titulo= "Asistente Inteligente"
        print(f"\n{titulo:_^30}")
        print("utilice palabra claves para sus consultas, como buscar, reptoducir o abrir")
        
    def registrar_usuario (self,):
        print("\n hola, bienvenido a tu asistente inteligente")
        nombre: str = input("ingresa tu nombre: ")
        email: str = input("ingresa tu email: ")
        self.asistente.registrar(nombre, email)

    def ejecutar_app(self):
        self.registrar_usuario()
        self.menu()
        c=""
        while c != "@":
            print("ingresa @ para salir")
            c= input("en que puedo ayudarte: ")
            if c != "@":
                self.asistente.analizar(c)
        