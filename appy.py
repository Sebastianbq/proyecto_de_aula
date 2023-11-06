import sys 
from interfaz import AsistenteInterfaz
from PyQt5.QtWidgets import QInputDialog, QApplication

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    nombre, ok1 = QInputDialog.getText(None, "Registro usuario", "nombre de usuario:")
    correo, ok2 = QInputDialog.getText(None, "Registro correo", "Correo electronico:")
    if not ok1 or not ok2:
        sys.exit()
    ventana = AsistenteInterfaz(nombre, correo)
    ventana.show()
    sys.exit(app.exec_())
