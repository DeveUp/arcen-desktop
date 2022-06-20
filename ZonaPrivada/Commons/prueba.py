
from tkinter import PhotoImage, Tk,Frame,Label,Button, font,Entry
import requests

class prueba (Frame):

    def contenido(self,fondoBarraDeContenido):
        fuente ="Verdana"
        fondoBarraDeContenido = self.fondoBarraDeContenido
       

        self.btnBloques=Button(self.fondoBarraDeContenido,text=" + Agregar",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w", command= lambda: prueba.argregarBloque(self,fondoBarraDeContenido ))
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
    

    def argregarBloque(self,fondoBarraDeContenido):
        

        print("llego")
        fuente ="Verdana"
        self.contenedor_agregar = Label(fondoBarraDeContenido,text="Principios de agregar", bg="#e0e0e0")
        self.contenedor_agregar.place(relx=0.1,rely=0.1,relwidth=0.7, relheight=0.7)

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
