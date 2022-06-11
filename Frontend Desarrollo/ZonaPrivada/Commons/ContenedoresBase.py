from msilib.schema import RadioButton
from tkinter import Tk,Frame,Label,Button


class ContenedoresBase (Frame):

    #Todo metodo dentro de una clase recibe self
    def __init__(self, master=None):

        super().__init__(master,width=screen_width, height=screen_height)
        self.master = master
        self.pack()
        self.construirContenedores()

    #Metodo para que muestre el mensaje desccrito
    def salir(self):
        self.lb = Label(raiz, text="prueba de btn de salida")
        self.lb.pack()#Posicionar lo que se creo dentro de la ventana
    
    def construirContenedores(self):

        # Se desarrolla un fondo con el objetivo de generar un borde en el cual se le pudiese cambiar el color
        
        borderColor = "#CCCCCC"

        self.fondoImgPrincipal = fondoImgPrincipal = Label(raiz,bg=borderColor)
        self.fondoImgPrincipal.place(relx=0,rely=0,relwidth=0.2, relheight=0.1)
        self.imgPrincipal = Label(fondoImgPrincipal,text="Imagen ufps", bg="#FFFFFF")
        self.imgPrincipal.place(relx=0,rely=0,relwidth=1, relheight=1)
    
        self.fondoNombreDependencia = fondoNombreDependencia = Label(raiz,bg=borderColor)
        self.fondoNombreDependencia.place(relx=0.2,rely=0,relwidth=0.5, relheight=0.10)
        self.nombreDependencia = Label(fondoNombreDependencia,text="Auxiliar de dependencia externa",  bg="#FFFFFF")
        self.nombreDependencia.place(relx=0,rely=0,relwidth=1, relheight=1)

        self.fondoBarraSalida = fondoBarraSalida = Label(raiz,bg=borderColor)
        self.fondoBarraSalida.place(relx=0.7,rely=0,relwidth=0.3, relheight=0.10)
        self.barraSalida = barraSalida= Label(fondoBarraSalida,text="Barra de salida", bg="#FFFFFF")
        self.barraSalida.place(relx=0,rely=0,relwidth=1, relheight=1)

        self.btnSalir=Button(self.barraSalida,text="SALIR",relief="flat",bg="#BC0017")
        self.btnSalir.place(relx=0.8,rely=0.1,relwidth=0.1, relheight=0.8,)

        self.usuario = nombreDependencia = Label(barraSalida,text="Leyner Ortega", bg="pink")
        self.usuario.place(relx=0.1,rely=0.1,relwidth=0.6, relheight=0.80)

        #BARRA LATERAL
        self.fondoBarraLateral = fondoBarraLateral = Label(raiz,bg=borderColor)
        self.fondoBarraLateral.place(relx=0.0,rely=0.1,relwidth=0.2, relheight=0.9)
        self.barraLateral =barraLateral= Label(fondoBarraLateral,text="Negocio",  bg="#FFFFFF")
        self.barraLateral.place(relx=0,rely=0,relwidth=1, relheight=1)

        self.contenedor = Label(barraLateral,text="contenedor1", bg="blue")
        self.contenedor.place(relx=0.1,rely=0.02,relwidth=0.8, relheight=0.05)

        self.contenedor1 = Label(barraLateral,text="contenedor1", bg="blue")
        self.contenedor1.place(relx=0.1,rely=0.09,relwidth=0.8, relheight=0.05)

        self.contenedor2 = Label(barraLateral,text="contenedor1", bg="blue")
        self.contenedor2.place(relx=0.1,rely=0.16,relwidth=0.8, relheight=0.05)

        self.contenedor3 = Label(barraLateral,text="contenedor1", bg="blue")
        self.contenedor3.place(relx=0.1,rely=0.23,relwidth=0.8, relheight=0.05)

        #BARRA DE CONTENIDO
        self.fondoBarraDeContenido = fondoBarraDeContenido = Label(raiz,bg=borderColor)
        self.fondoBarraDeContenido.place(relx=0.2,rely=0.1,relwidth=0.8, relheight=0.9)
        self.barraDeContenido = Label(fondoBarraDeContenido,text="Inicio",  bg="#FFFFFF")
        self.barraDeContenido.place(relx=0,rely=0,relwidth=1, relheight=1)






raiz = Tk()
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
raiz.title("Secretaria general de la UFPS")
raiz.geometry(str(screen_width)+"x"+str(screen_height)) 
app = ContenedoresBase(raiz) 
app.mainloop()
