from msilib.schema import Font
from tkinter import PhotoImage, Tk,Frame,Label,Button, font,Entry
from unicodedata import name
from PIL import Image, ImageTk
import requests
#from fuentes import fuentes
#from prueba import prueba
from ZonaPrivada.Commons.barra_de_navegacion import barra_de_navegacion




class ContenedoresPrueba (Frame):

    #Metodo para que muestre el mensaje desccrito
    # def salir(self):
    #     self.lb = Label(raiz, text="prueba de btn de salida")
    #     self.lb.pack()#Posicionar lo que se creo dentro de la ventana
    
    def construirContenedores(self,raiz):

        
        fuente ="Verdana"
        # Se desarrolla un fondo con el objetivo de generar un borde en el cual se le pudiese cambiar el color
        
        borderColor = "#FFF2F2"

        self.fondoImgPrincipal = fondoImgPrincipal = Label(raiz,bg=borderColor)
        self.fondoImgPrincipal.place(relx=0,rely=0,relwidth=0.2, relheight=0.1)
        self.imgPrincipal = Label(fondoImgPrincipal,text="Imagen ufps", bg="#FFFFFF")
        self.imgPrincipal.place(relx=0,rely=0,relwidth=1, relheight=1)

        widthImg = self.imgPrincipal.winfo_screenwidth()*(0.2)
        heightImg = self.imgPrincipal.winfo_screenheight()*(0.1)

        print(widthImg)
        print(heightImg)

        #Cargar imagenes sin importar el formato
        self.image = Image.open('ZonaPublica\Img\Imagen\logoUFPS.png')
        self.resize_image = self.image.resize((int(widthImg), int(heightImg)))
        self.python_image = ImageTk.PhotoImage(self.resize_image)
        self.image_label = Label(self.fondoImgPrincipal, image=self.python_image).pack()
    
        

        self.fondoNombreDependencia = fondoNombreDependencia = Label(raiz,bg=borderColor)
        self.fondoNombreDependencia.place(relx=0.2,rely=0,relwidth=0.5, relheight=0.10)
        self.nombreDependencia = Label(fondoNombreDependencia,text="Auxiliar de dependencia externa",  bg="#FFFFFF", font=fuente)
        self.nombreDependencia.place(relx=0,rely=0,relwidth=1, relheight=1)
        



        self.fondoBarraSalida = fondoBarraSalida = Label(raiz,bg=borderColor)
        self.fondoBarraSalida.place(relx=0.7,rely=0,relwidth=0.3, relheight=0.10)
        self.barraSalida = barraSalida= Label(fondoBarraSalida,text="Barra de salida", bg="#FFFFFF")
        self.barraSalida.place(relx=0,rely=0,relwidth=1, relheight=1)
        
       
      
    
        self.btnSalir=Button(self.barraSalida,text="Salir", bg="#BC0017", foreground="#FFFFFF", font=fuente, relief="flat")
        self.btnSalir.place(relx=0.8,rely=0.1,relwidth=0.2, relheight=0.8)

       

        self.usuario = nombreDependencia = Label(barraSalida,text="Leyner Ortega", bg="#FFFFFF", font=fuente)
        self.usuario.place(relx=0.1,rely=0.1,relwidth=0.6, relheight=0.80)


        #BARRA DE CONTENIDO
        self.fondoBarraDeContenido = fondoBarraDeContenido = Label(raiz,bg=borderColor)
        self.fondoBarraDeContenido.place(relx=0.2,rely=0.1,relwidth=0.8, relheight=0.9)
        self.barraDeContenido = Label(fondoBarraDeContenido,text="Inicio",  bg="#FFFFFF")
        self.barraDeContenido.place(relx=0,rely=0,relwidth=1, relheight=1)

        #BARRA LATERAL
        #Base de la barra lateral 
        self.fondoBarraLateral = fondoBarraLateral = Label(raiz,bg=borderColor)
        self.fondoBarraLateral.place(relx=0.0,rely=0.1,relwidth=0.2, relheight=0.9)
        self.barraLateral =barraLateral= Label(fondoBarraLateral,text="Negocio",  bg="#FFFFFF")
        self.barraLateral.place(relx=0,rely=0,relwidth=1, relheight=1)

        barra_de_navegacion.navegacion(self,barraLateral,fondoBarraDeContenido)



    

