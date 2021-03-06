import email
import imp
from tkinter import Tk,Frame,Label,Button,Entry
from xml.dom.expatbuilder import DOCUMENT_NODE
from PIL import Image, ImageTk
from ZonaPrivada.Commons.ContenedorPrueba import ContenedoresPrueba
import requests
import json
class Login (Frame):
    
    def crearMaquetaBase(self, raiz):

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
        self.txtNum1=Entry(raiz,bg="#CCCCCC", font=fuente)
        self.txtNum1.place(relx=0.70,rely=0.5,relwidth=0.2, relheight=0.05)

        self.lblNum2 = Label(raiz,text="Documento", font=fuente)
        self.lblNum2.place(relx=0.70,rely=0.55,relwidth=0.2, relheight=0.05)
        self.txtNum2=Entry(raiz,bg="#CCCCCC", font=fuente)
        self.txtNum2.place(relx=0.70,rely=0.6,relwidth=0.2, relheight=0.05)


        self.lblNum3 = Label(raiz,text="Contrase??a", font=fuente)
        self.lblNum3.place(relx=0.70,rely=0.65,relwidth=0.2, relheight=0.05)
        self.txtNum3=Entry(raiz,bg="#CCCCCC",show="???")
        self.txtNum3.place(relx=0.70,rely=0.7,relwidth=0.2, relheight=0.05)

        email=self.txtNum1.get()
        documento =self.txtNum2.get()
        contrase??a = self.txtNum3.get()

        
        #Crear botones
        #self.btn=Button(raiz,text="Iniciar sesion", command=self.funcionalidad.iniciarSession(fondoLogin))
        self.btn=Button(raiz,text="Iniciar sesion", bg="#BC0017", foreground="#FFFFFF", font=fuente,command=lambda: Login.peticionPOST(self,email,documento, contrase??a))
        self.btn.place(relx=0.70,rely=0.8,relwidth=0.2, relheight=0.05)
        print("si llega 1")
        

        #command=lambda: bloques.contenido(self,self.fondoBarraDeContenido)
        return raiz

        
    def peticionPOST(self, raiz, email, documento, contrase??a):
        print(email)
        print("LLEGA AL POST")
        #print(documento)
        #print(contrase??a)
        url = 'http://httpbin.org/post'
        login_request ={'email':email,'documento':documento, 'contrase??a':contrase??a}

        response = requests.post(url,data=json.dumps(login_request))
        print(response.url)

        if response.status_code==200:
            print("ARCEN status_code =200")
            #Login.destroy()
            ContenedoresPrueba.construirContenedores(self,raiz)
            



    def iniciarSession(self, raiz):
        print("si llega555555555555555")
        self.lb = Label(raiz, text="Se registra intento de inicio de session RRRRRRRRRRR",bg="red")
        self.lb.place(relx=0.0, rely=0.0,relwidth=0.8, relheight=0.05)
        #self.lb.pack()#Posicionar lo que se creo dentro de la ventana
    