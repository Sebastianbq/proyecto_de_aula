from dataclasses import dataclass
import spacy

@dataclass
class Usuario:
    nombre: str
    email: str
    

class Asistente:
    def __init__(self):
        self.consulta: str
        self.usuario: Usuario
        self.google: Google= Google()
        self.youtube: Youtube= Youtube()
        self.calculadora: Calculadora= Calculadora()

    def registrar(self,nombre: str, email:str):
        self.usuario = Usuario(nombre,email)

    def analizar(self, consulta) -> str:
        npl= spacy.load("es_core_news_sm")
        self.consulta= npl(consulta)
        for determinar in self.consulta:
            if determinar.text.lower() == "buscar":
                ejecutar= "Google"
                return ejecutar
            elif determinar.text.lower() == "reproducir":
                ejecutar= "youtube"
                return ejecutar
            elif determinar.text.lower() == "calculadora":
                ejecutar= "calculadora"
                return ejecutar


class Youtube:
    pass


class Google:
    pass


class Calculadora:
    pass

