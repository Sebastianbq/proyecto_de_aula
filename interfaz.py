import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QInputDialog, QDialog, QLabel, QLineEdit
from modelo.asistente import Asistente



class VentanaCalculadora(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ingresa Calculadora')
        layout= QVBoxLayout()

        etiqueta= QLabel("Ingresa la direccion de la calculadora (por ejemplo, c:\\window\\System32...)")
        layout.addWidget(etiqueta)

        self.campo_direccion =QLineEdit()
        layout.addWidget(self.campo_direccion)

        boton= QPushButton ("confirmar")
        boton.clicked.connect(self.obtener_direccion)
        layout.addWidget(boton)
        
        self.setLayout(layout)

    def obtener_direccion(self):
        direccion= self.campo_direccion.text()
        self.accept()



class AsistenteInterfaz(QWidget):
    def __init__(self, nombre: str, correo: str):
        super().__init__()
        self.initUI(nombre)
        self.nombre= nombre
        self.correo= correo        
        self.asistente= Asistente()            
        self.asistente.registrar(nombre, correo)


    def initUI(self,nombre: str):
        self.setWindowTitle('Asistente Inteligente')
        
        self.entrada_usuario = QTextEdit(self)
        self.boton_enviar = QPushButton('Enviar', self)
        self.boton_enviar.clicked.connect(self.procesar_entrada)

         
        mostrar_menu= self.menu(nombre)        
        self.salida_asistente = QTextEdit(self)
        self.salida_asistente.setPlainText(mostrar_menu)
        
        self.salida_asistente.setReadOnly(True)


        layout = QVBoxLayout()
        layout.addWidget(self.salida_asistente)        
        layout.addWidget(self.entrada_usuario)
        layout.addWidget(self.boton_enviar)

        self.setLayout(layout)


    def menu(self,nombre:str):
        return f"Hola {nombre}, bienvenido a tu asistente inteligente \nUtiliza palabras claves para tus consultas como:\n buscar, reproducir o abrir \n"



    def procesar_entrada(self):
        
        entrada = self.entrada_usuario.toPlainText()        
        respuesta = self.asistente.analizar(entrada)
        if respuesta == "direccion":
            ventanacal= VentanaCalculadora()
            resultado= ventanacal.exec_()
            direccion= ventanacal.campo_direccion.text() 
            respuesta= self.asistente.registro_calculadora(direccion)
        self.entrada_usuario.setPlainText("")
        self.salida_asistente.append(f"{self.nombre}: {entrada}")
        self.salida_asistente.append(f"Asistente: {respuesta} \n")  

