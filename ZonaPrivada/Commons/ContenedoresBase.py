
from msilib.schema import Font
from tkinter import PhotoImage, Tk,Frame,Label,Button, font,Entry
from unicodedata import name
from PIL import Image, ImageTk
import requests
from fuentes import fuentes


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
        fuente ="Verdana"
        # Se desarrolla un fondo con el objetivo de generar un borde en el cual se le pudiese cambiar el color
        
        borderColor = "#FFF2F2"

        self.fondoImgPrincipal = fondoImgPrincipal = Label(raiz,bg=borderColor)
        self.fondoImgPrincipal.place(relx=0,rely=0,relwidth=0.2, relheight=0.1)
        self.imgPrincipal = Label(fondoImgPrincipal,text="Imagen ufps", bg="#FFFFFF")
        self.imgPrincipal.place(relx=0,rely=0,relwidth=1, relheight=1)

        #self.imagenPrincipal = PhotoImage(file="Frontend Desarrollo\ZonaPublica\Img\Imagen\logoUFPS.png")
        #self.lblImg = Label(fondoImgPrincipal, image=self.imagenPrincipal)
        #self.place(relx=0,rely=0,relwidth=1, relheight=1)
        #self.lblImg.pack

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

       

        self.usuario = nombreDependencia = Label(barraSalida,text="Leyner Ortega", bg="#FFF2F2", font=fuente)
        self.usuario.place(relx=0.1,rely=0.1,relwidth=0.6, relheight=0.80)


         #BARRA DE CONTENIDO
        self.fondoBarraDeContenido = fondoBarraDeContenido = Label(raiz,bg=borderColor)
        self.fondoBarraDeContenido.place(relx=0.2,rely=0.1,relwidth=0.8, relheight=0.9)
        self.barraDeContenido = Label(fondoBarraDeContenido,text="Inicio",  bg="#FFFFFF")
        self.barraDeContenido.place(relx=0,rely=0,relwidth=1, relheight=1)

        #BARRA LATERAL
        self.fondoBarraLateral = fondoBarraLateral = Label(raiz,bg=borderColor)
        self.fondoBarraLateral.place(relx=0.0,rely=0.1,relwidth=0.2, relheight=0.9)
        self.barraLateral =barraLateral= Label(fondoBarraLateral,text="Negocio",  bg="#FFFFFF")
        self.barraLateral.place(relx=0,rely=0,relwidth=1, relheight=1)

        self.contenedor0 = Label(barraLateral,text="contenedor1", bg="#CCCCCC", font=fuente)
        self.contenedor0.place(relx=0.1,rely=0.02,relwidth=0.8, relheight=0.05)
        self.btnBloques=Button(self.contenedor0,text="Bloques", bg="#FFFFFF", font=fuente, relief="flat", anchor="w", command =self.contenido)
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)

        self.contenedor1 = Label(barraLateral,text="contenedor1", bg="#CCCCCC", font=fuente)
        self.contenedor1.place(relx=0.1,rely=0.09,relwidth=0.8, relheight=0.05)
        self.btnBloques=Button(self.contenedor1,text="Muebles", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)


        self.contenedor2 = Label(barraLateral,text="contenedor1", bg="#CCCCCC", font=fuente)
        self.contenedor2.place(relx=0.1,rely=0.16,relwidth=0.8, relheight=0.05)
        self.btnBloques=Button(self.contenedor2,text="Estantes", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)


        self.contenedor3 = Label(barraLateral,text="contenedor1", bg="#CCCCCC", font=fuente)
        self.contenedor3.place(relx=0.1,rely=0.23,relwidth=0.8, relheight=0.05)
        self.btnBloques=Button(self.contenedor3,text="Cajas", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)


       

        #self.contenido()
        


    def contenido(self):
        fuente ="Verdana"
        
        self.btnBloques=Button(self.fondoBarraDeContenido,text=" + Agregar",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w", command=self.argregar)
        self.btnBloques.place(relx=0.8,rely=0.05,relwidth=0.1, relheight=0.05)
        
        self.contenedor3 = Label(self.fondoBarraDeContenido,text="", bg="#FFF2F2")
        self.contenedor3.place(relx=0.1,rely=0.1,relwidth=0.8, relheight=0.8)
        

        API = 'https://jsonplaceholder.typicode.com/users'  
        json_datos = requests.get(API).json()
        nombre=""
        numero =1
        while numero<=10:
        
            API = 'https://jsonplaceholder.typicode.com/users/'+str(numero)  
            json_datos = requests.get(API).json()
            nombre =str(json_datos["username"]) 
            self.lb = Label(self.contenedor3, text=nombre,font=fuente, anchor="w",bg="#BC0017")
            self.lb.place(relwidth=0.7, relheight=0.2)
            self.lb.pack(anchor="w")#Posicionar lo que se creo dentro de la ventana

            self.btnBloques=Button(self.contenedor3,text=" - Eliminar",  bg="#BC0017", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w",  command=self.validacionCliente)
            self.btnBloques.pack(anchor="ne")
            numero += 1
        

        #for key in json_datos:
        #    print(key, ":", json_datos[key])
    


    def validacionCliente(self):

        fuente ="Verdana"

        self.contenedorCliente = Label(self.fondoBarraDeContenido,text="", bg="red")
        self.contenedorCliente.place(relx=0.3,rely=0.3,relwidth=0.4, relheight=0.4)

        self.msgConnfirmacion = barraSalida= Label(self.contenedorCliente,text="¿Desea eliminar el registro?", bg="#CCCCCC", font=fuente)
        self.msgConnfirmacion.place(relx=0.2,rely=0.2,relwidth=0.6, relheight=0.2)

        self.btnSi=Button(self.contenedorCliente,text=" SI ",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat")
        self.btnSi.place(relx=0.2,rely=0.6,relwidth=0.2, relheight=0.2)

        self.btnNo=Button(self.contenedorCliente,text=" NO ",  bg="#BC0017", foreground="#FFFFFF", font=fuente, relief="flat")
        self.btnNo.place(relx=0.6,rely=0.6,relwidth=0.2, relheight=0.2)

    def argregar(self):

        fuente ="Verdana"
        self.contenedor_agregar = Label(self.fondoBarraDeContenido,text="Principios de agregar", bg="red")
        self.contenedor_agregar.place(relx=0.1,rely=0.1,relwidth=0.8, relheight=0.8)

        self.titulo_agregar = Label(self.contenedor_agregar,text="AGREGAR BLOQUE", bg="#CCCCCC",font=fuente)
        self.titulo_agregar.place(relx=0.05,rely=0.05,relwidth=0.9, relheight=0.2)
        
        self.info_letra = Label(self.contenedor_agregar,text="Info", bg="#CCCCCC",font=fuente)
        self.info_letra.place(relx=0.1,rely=0.3,relwidth=0.8, relheight=0.1)
        
        self.txtNum2=Entry(self.contenedor_agregar,bg="#CCCCCC")
        self.txtNum2.place(relx=0.10,rely=0.45,relwidth=0.8, relheight=0.05) 
        
        self.info_piso = Label(self.contenedor_agregar,text="Info", bg="#CCCCCC",font=fuente)
        self.info_piso.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.1)

        self.txtNum2=Entry(self.contenedor_agregar,bg="#CCCCCC")
        self.txtNum2.place(relx=0.1,rely=0.75,relwidth=0.8, relheight=0.05)

        self.btnBloques=Button(self.contenedor_agregar,text=" Guardar",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.8,rely=0.9,relwidth=0.1, relheight=0.05)



    #def guardar(self):
    #    return None


    



        



raiz = Tk()
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
print(screen_width)
print(screen_height)
raiz.title("Secretaria general de la UFPS")
# Añadir icono del lado derecho de la ventana con la (Ruta relativa)
raiz.iconbitmap('ZonaPublica\Img\Ico\logoufps.ico')
raiz.geometry(str(screen_width)+"x"+str(screen_height)) 
app = ContenedoresBase(raiz) 
app.mainloop()
