import subprocess


class Calculadora:
    def __init__(self):
        pass

    def abrir(self, calculadora):
        try:
            subprocess.run([calculadora])
            ejecutar= "se abrio exitosamente"        
            return ejecutar
        except FileNotFoundError:
            ejecutar= "no se pudo encontrar la calcuadora en la ubicacion dada"
            return ejecutar
        except PermissionError:
            ejecutar= "No tienes acceso a la aplicacion o al archivo "
            return ejecutar