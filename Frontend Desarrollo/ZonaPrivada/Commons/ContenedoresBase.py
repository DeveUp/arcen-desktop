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
        #BARRA SUPERIOR
        self.imgPrincipal = Label(raiz,text="Imagen ufps", bg="#06283D")
        self.imgPrincipal.place(relx=0,rely=0,relwidth=0.20, relheight=0.10)
        self.imgPrincipal.config(cursor="heart", relief="flat")

        self.nombreDependencia = Label(raiz,text="Auxiliar de dependencia externa", bg="pink")
        self.nombreDependencia.place(relx=0.2,rely=0,relwidth=0.5, relheight=0.10)

        self.barraSalida = barraSalida= nombreDependencia = Label(raiz,text="Barra de salida", bg="yellow")
        self.barraSalida.place(relx=0.7,rely=0,relwidth=0.3, relheight=0.10)

        self.btnSalir=Button(self.barraSalida,text="SALIR")
        self.btnSalir.place(relx=0.8,rely=0.1,relwidth=0.1, relheight=0.8,)

        self.usuario = nombreDependencia = Label(barraSalida,text="Leyner Ortega", bg="pink")
        self.usuario.place(relx=0.1,rely=0.1,relwidth=0.6, relheight=0.80)

        #BARRA LATERAL
        self.barraLateral = Label(raiz,text="Negocio", bg="pink")
        self.barraLateral.place(relx=0.0,rely=0.1,relwidth=0.2, relheight=0.9)

        #BARRA DE CONTENIDO
        self.barraDeContenido = Label(raiz,text="Inicio", bg="red")
        self.barraDeContenido.place(relx=0.2,rely=0.1,relwidth=0.8, relheight=0.9)




raiz = Tk()
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
raiz.title("Secretaria general de la UFPS")
raiz.geometry(str(screen_width)+"x"+str(screen_height)) 
app = ContenedoresBase(raiz) 
app.mainloop()
