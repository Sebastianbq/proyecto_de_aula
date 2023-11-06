from modelo.youtube import Youtube
from modelo.calculadora import Calculadora
from modelo.google import Google


class Usuario:
    def __init__(self,nombre: str, email: str):
        self.nombre= nombre
        self.email= email
        
    

class Asistente:
    def __init__(self):
        self.consulta: str
        self.usuario: Usuario = Usuario("","")
        self.google: Google= Google()
        self.youtube: Youtube= Youtube()
        self.calculadora: Calculadora= Calculadora()

    def cargar_datos(self):
        with open("contenidos.txt", "r") as archivo:
            datos= []
            for x in archivo:
                datos.append(x.split())   
            return datos


    def registrar(self,nombre: str, email:str):
        datos= self.cargar_datos()
        for i in range(len(datos)):
            if email in datos[i]:                
                self.usuario= Usuario(nombre, email)
                return 
        self.usuario = Usuario(nombre, email)
        with open("contenidos.txt", "a") as archivo:
            archivo.write(f"\n\nnombre: {nombre}")
            archivo.write(f"\ncorreo: {email}")        

    def analizar(self, consulta) -> str:
        analiza= consulta.split()
        datos= self.cargar_datos()
        if len(analiza) == 0:
            analiza.append("0")  
        for i in range(len(analiza)):
            if analiza[i] == "buscar":
                ejecutar= self.google.buscar_google(consulta)
                return "se ejecuto el buscador de google"
            elif analiza[i] == "reproducir":
                ejecutar= self.youtube.reproducir(consulta)
                return "se ejecuto el reproductor de youtube"
            elif analiza[i] == "abrir":
                for i in range(len(datos)):
                    for i in range(len(datos)):                        
                        if self.usuario.email in datos[i]:                            
                            try :
                                if "calculadora:" in datos[i+1]:                                  
                                    direccion= datos[i+1][1]
                                    print(direccion)         
                                    ejecutar= self.calculadora.abrir(direccion)                                
                                    return ejecutar 
                            except IndexError:
                                pass
                    calculadora= "direccion"
                    return calculadora                
        else:
            ejecutar= "utiliza palabras claves"
            return ejecutar

    def registro_calculadora(self, calculadora):
        with open("contenidos.txt", "a") as archivo:
            archivo.write(f"\ncalculadora: {calculadora} ")
        ejecutar= self.calculadora.abrir(calculadora)
        return ejecutar



