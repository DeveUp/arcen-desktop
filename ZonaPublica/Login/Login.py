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

        fuente ="Verdana"

        self.fondo= Label(raiz)
        self.fondo.place(relx=0,rely=0,relwidth=1, relheight=1)

        self.fondoLoginImg= Label(raiz)
        self.fondoLoginImg.place(relx=0.0,rely=0.0,relwidth=0.7, relheight=1)

        widthImg = raiz.winfo_screenwidth()*0.7
        heightImg = raiz.winfo_screenheight()

        print(widthImg)
        print(heightImg)

        #Cargar imagenes sin importar el formato
        self.image = Image.open('ZonaPublica\Img\Imagen\login.png')
        self.resize_image = self.image.resize((int(widthImg), int(heightImg)))
        self.python_image = ImageTk.PhotoImage(self.resize_image)
        self.image_label = Label(self.fondoLoginImg, image=self.python_image).pack()

        self.fondoLogin= Label(raiz)
        self.fondoLogin.place(relx=0.6,rely=0.0,relwidth=0.4, relheight=1)

        self.imgSecundaria = Label(raiz,text="Imagen ufps")
        self.imgSecundaria.place(relx=0.7,rely=0.05,relwidth=0.2, relheight=0.4)

        widthImgSec = raiz.winfo_screenwidth()*0.2
        heightImgSec = raiz.winfo_screenheight()*0.3

        print(widthImgSec)
        print(heightImgSec)

        #Cargar imagenes sin importar el formato
        self.imageSec = Image.open('ZonaPublica\Img\Imagen\logoUFPS2.png')
        self.resize_imageSec = self.imageSec.resize((int(widthImgSec), int(heightImgSec)))
        self.python_imageSec = ImageTk.PhotoImage(self.resize_imageSec)
        self.image_labelSec = Label(self.imgSecundaria, image=self.python_imageSec).pack()


        self.lblNum1 = Label(raiz,text="Email", font=fuente)
        self.lblNum1.place(relx=0.70,rely=0.45,relwidth=0.2, relheight=0.05)
        self.txtNum1=Entry(raiz,bg="#CCCCCC")
        self.txtNum1.place(relx=0.70,rely=0.5,relwidth=0.2, relheight=0.05)

        self.lblNum2 = Label(raiz,text="Documento", font=fuente)
        self.lblNum2.place(relx=0.70,rely=0.55,relwidth=0.2, relheight=0.05)
        self.txtNum2=Entry(raiz,bg="#CCCCCC")
        self.txtNum2.place(relx=0.70,rely=0.6,relwidth=0.2, relheight=0.05)


        self.lblNum3 = Label(raiz,text="Contraseña", font=fuente)
        self.lblNum3.place(relx=0.70,rely=0.65,relwidth=0.2, relheight=0.05)
        self.txtNum2=Entry(raiz,bg="#CCCCCC")
        self.txtNum2.place(relx=0.70,rely=0.7,relwidth=0.2, relheight=0.05)

        #Crear botones
        #self.btn=Button(raiz,text="Iniciar sesion", command=self.funcionalidad.iniciarSession(fondoLogin))
        self.btn=Button(raiz,text="Iniciar sesion", bg="#BC0017", foreground="#FFFFFF", font=fuente)
        self.btn.place(relx=0.70,rely=0.8,relwidth=0.2, relheight=0.05)
        print("si llega 1")
        
        return raiz

        




    def iniciarSession(self):
        print("si llega555555555555555")
        self.lb = Label(raiz, text="Se registra intento de inicio de session RRRRRRRRRRR",bg="red")
        self.lb.place(relx=0.0, rely=0.0,relwidth=0.8, relheight=0.05)
        #self.lb.pack()#Posicionar lo que se creo dentro de la ventana
    

raiz = Tk()
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
# Añadir icono del lado derecho de la ventana con la (Ruta relativa)
raiz.iconbitmap('ZonaPublica\Img\Ico\logoufps.ico')
raiz.title("Secretaria general de la UFPS")
raiz.geometry(str(screen_width)+"x"+str(screen_height)) 
app = Login(raiz) 
app.mainloop()