from tkinter import Tk,Frame
from ZonaPrivada.Commons.ContenedorPrueba import ContenedoresPrueba
from ZonaPublica.Login.Login import Login


class Main(Frame):

    def __init__(self, master=None):
       
        super().__init__(master,width=screen_width, height=screen_height)
        self.master = master
        self.pack()
        Login.crearMaquetaBase(self, raiz)
        #self.crearMaquetaBase()
    

# Se construye la base desde la cual se crean todos los containers
raiz = Tk()

# Captura el tamaño de la pantalla desde la cual se esta ejecutando la applicacion y construye el container.
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
raiz.geometry(str(screen_width)+"x"+str(screen_height))

# Añadir icono del lado derecho de la ventana con la (Ruta relativa)
raiz.iconbitmap('ZonaPublica\Img\Ico\logoufps.ico')

# Anade el titulo
raiz.title("Secretaria general de la UFPS")


app = Main(raiz) 
app.mainloop()