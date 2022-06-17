from tkinter import Tk,Frame,Label,Button

class Clase2 ():

    #Todo metodo dentro de una clase recibe self
    #def __init__(self, master=None):
       
    #    super().__init__(master,width=1, height=1)
    #    self.master = master
    #    self.pack()
    #    self.crearMaquetaBase()

    

    def iniciarSession(self, base):
        print("si llega555555555555555")
        self.lb = Label(base, text="Se registra intento de inicio de session RRRRRRRRRRR",bg="yellow")
        self.lb.place(relx=0.0, rely=0.0,relwidth=0.8, relheight=0.05)
        #self.lb.pack()#Posicionar lo que se creo dentro de la ventana
    
    def iniciarDev(self, base):
        print("si llega555555555555555dfbngfhkdjfg")
        self.lb = Label(base, text="Son RRRRRRRRRRRjghdkjsghfdj",)
        self.lb.place(relx=0.0, rely=0.0,relwidth=0.8, relheight=0.05)
        #self.lb.pack()#Posicionar lo que se creo dentro de la ventana


#raiz = Tk()
#app = Clase2(raiz) 

