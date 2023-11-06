import webbrowser

class Google:
    def __init__(self):
        pass
    
    def buscar_google(self, consulta):
        url_google= "https://www.google.com/search?q="
        consulta= consulta.replace("buscar","")
        consulta= consulta.lstrip()
        buscar= consulta.replace(" ", "+")
        url= url_google + buscar
        print(url)
        webbrowser.open(url)
        
