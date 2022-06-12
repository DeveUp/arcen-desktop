from tkinter import Tk,Frame,Label,Button,Entry
from PIL import Image, ImageTk
from Clase2 import *

class Login (Frame):

    funcionalidad = Clase2()
    #Todo metodo dentro de una clase recibe self
    def __init__(self, master=None):
       
        super().__init__(master,width=screen_width, height=screen_height)
        self.master = master
        self.pack()
        self.crearMaquetaBase()

    

    def crearMaquetaBase(self):
        self.fondo= Label(raiz, bg="white")
        self.fondo.place(relx=0,rely=0,relwidth=1, relheight=1)

        widthImg = raiz.winfo_screenwidth()
        heightImg = raiz.winfo_screenheight()

        print(widthImg)
        print(heightImg)

        #Cargar imagenes sin importar el formato
        self.image = Image.open('Frontend Desarrollo\ZonaPublica\Img\Imagen\login2.jpeg')
        self.resize_image = self.image.resize((int(widthImg), int(heightImg)))
        self.python_image = ImageTk.PhotoImage(self.resize_image)
        self.image_label = Label(self.fondo, image=self.python_image).pack()

        self.fondoLogin= Label(raiz, bg="white")
        self.fondoLogin.place(relx=0.65,rely=0.15,relwidth=0.3, relheight=0.7)

        self.imgSecundaria = Label(raiz,text="Imagen ufps", bg="red")
        self.imgSecundaria.place(relx=0.70,rely=0.20,relwidth=0.2, relheight=0.1)

        self.lblNum1 = Label(raiz,text="Email",bg="yellow")
        self.lblNum1.place(relx=0.70,rely=0.35,relwidth=0.2, relheight=0.05)
        self.txtNum1=Entry(raiz,bg="pink")
        self.txtNum1.place(relx=0.70,rely=0.4,relwidth=0.2, relheight=0.05)

        self.lblNum2 = Label(raiz,text="Documento",bg="yellow")
        self.lblNum2.place(relx=0.70,rely=0.45,relwidth=0.2, relheight=0.05)
        self.txtNum2=Entry(raiz,bg="pink")
        self.txtNum2.place(relx=0.70,rely=0.5,relwidth=0.2, relheight=0.05)


        self.lblNum3 = Label(raiz,text="Contraseña",bg="yellow")
        self.lblNum3.place(relx=0.70,rely=0.55,relwidth=0.2, relheight=0.05)
        self.txtNum2=Entry(raiz,bg="pink")
        self.txtNum2.place(relx=0.70,rely=0.6,relwidth=0.2, relheight=0.05)

        #Crear botones
        #self.btn=Button(raiz,text="Iniciar sesion", command=self.funcionalidad.iniciarSession(fondoLogin))
        self.btn=Button(raiz,text="Iniciar sesion")
        self.btn.place(relx=0.70,rely=0.7,relwidth=0.2, relheight=0.05)
        print("si llega 1")

        




    def iniciarSession(self):
        print("si llega555555555555555")
        self.lb = Label(raiz, text="Se registra intento de inicio de session RRRRRRRRRRR",bg="red")
        self.lb.place(relx=0.0, rely=0.0,relwidth=0.8, relheight=0.05)
        #self.lb.pack()#Posicionar lo que se creo dentro de la ventana
    

raiz = Tk()
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
raiz.title("Secretaria general de la UFPS")
raiz.geometry(str(screen_width)+"x"+str(screen_height)) 
app = Login(raiz) 
app.mainloop()
