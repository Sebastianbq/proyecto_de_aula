import webbrowser

class Youtube:
    def __init__(self):
        pass
    
    def reproducir(self,consulta):
        url_youtube = "https://www.youtube.com/results?search_query="
        consulta= consulta.replace("reproducir","")
        consulta= consulta.lstrip()
        buscar= consulta.replace(" ", "+")
        url= url_youtube + buscar
        print(url)
        webbrowser.open(url)
        return