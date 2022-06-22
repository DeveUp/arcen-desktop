from shutil import which
from tkinter import PhotoImage, Tk,Frame,Label,Button, font,Entry,filedialog
import requests
import json

class digitalizar (Frame):

    def contenido(self,fondoBarraDeContenido):
        fuente ="Verdana"
        fondoBarraDeContenido = self.fondoBarraDeContenido
       

        # self.btn_agregar=Button(self.fondoBarraDeContenido,text=" + Agregar",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w", command= lambda: bloques.argregarBloque(self,fondoBarraDeContenido ))
        # self.btn_agregar.place(relx=0.8,rely=0.05,relwidth=0.1, relheight=0.05)
        
        self.contenedor3 = Label(self.fondoBarraDeContenido,text="THIS IS PARA digitalizar", bg="#FFF2F2")
        self.contenedor3.place(relx=0.1,rely=0.1,relwidth=0.8, relheight=0.8)
        
        self.btn_agregar=Button(self.contenedor3,text=" + abir archivo",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w", command= lambda: digitalizar.abir_archivo(self))
        self.btn_agregar.place(relx=0.4,rely=0.4,relwidth=0.2, relheight=0.2)
        


    def abir_archivo(self):
        archivo = filedialog.askopenfilename(title="Archivo", initialdir="C:/Users/leyner.ortega_pragma/Documents/[LEYNER]/UFPS/Secretaria/Documentos digitalizados")


        # API = 'https://jsonplaceholder.typicode.com/comments'  
        # json_datos = requests.get(API).json()
        # nombre=""
        
        # #datos =json_datos[3]
        # posicion_y=0.0

        # for datos in json_datos:
        
        #     # name = json_datos[1]
        #     # print(name)
        #     self.contenedor_lista = Label(self.contenedor3, text="prueba")
        #     self.contenedor_lista.place(relx=0.0, rely=posicion_y, relwidth=1, relheight=0.1)
        #     nombre = datos.get("name")
        #     self.lb = Label(self.contenedor_lista, text=nombre,font=fuente, anchor="w",bg="#FFFFFF")
        #     self.lb.place(relx=0.0, rely=0.0,relwidth=0.85, relheight=1)


        #     self.btnBloques=Button(self.contenedor_lista,text=" - Eliminar",  bg="#BC0017", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w",  command=lambda: tipos_bloques.validacionCliente(self))
        #     self.btnBloques.place(relx=0.86, rely=0.15,relwidth=0.15, relheight=0.7)
        #     #numero += 1
        #     posicion_y+=0.1
        #     print(posicion_y)

        #     if posicion_y==1.2:
        #         self.btn_agregar=Button(self.fondoBarraDeContenido,text=" Siguiente pagina >",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w", command= lambda: tipos_bloques.contenido(self,fondoBarraDeContenido ))
        #         self.btn_agregar.place(relx=0.7,rely=0.9,relwidth=0.2, relheight=0.05)

        


        #posicion_y=0.0
        # while numero<=10:
        # #command= lambda: prueba.argregarBloque(self,fondoBarraDeContenido )
        # #command=self.validacionCliente
        #     self.contenedor_lista = Label(self.contenedor3, text="prueba")
        #     self.contenedor_lista.place(relx=0.0, rely=posicion_y, relwidth=1, relheight=0.1)
            
        #     API = 'https://jsonplaceholder.typicode.com/users/'+str(numero)  
           
        #     json_datos = requests.get(API).json()
        #     nombre =str(json_datos["username"]) 
        #     self.lb = Label(self.contenedor_lista, text=nombre,font=fuente, anchor="w",bg="#FFFFFF")
        #     self.lb.place(relx=0.0, rely=0.0,relwidth=0.85, relheight=1)
        #     #self.lb.pack(padx=10, pady=10)
        #     #self.lb.pack(anchor="w")#Posicionar lo que se creo dentro de la ventana

        #     self.btnBloques=Button(self.contenedor_lista,text=" - Eliminar",  bg="#BC0017", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w",  command=lambda: bloques.validacionCliente(self))
        #     self.btnBloques.place(relx=0.86, rely=0.15,relwidth=0.15, relheight=0.88)

        #     #self.btnBloques.pack(anchor="ne")
        #     numero += 1
        #     posicion_y+=0.1
        #     print(numero)

        
    

    # def argregarBloque(self,fondoBarraDeContenido):
        
    #     self.contenedor3.destroy()
    #     self.btn_agregar.destroy()
    #     print("llego")
    #     fuente ="Verdana"
    #     self.contenedor_agregar = Label(fondoBarraDeContenido)
    #     self.contenedor_agregar.place(relx=0.1,rely=0.1,relwidth=0.8, relheight=0.8)

    #     self.titulo_agregar = Label(self.contenedor_agregar,text="AGREGAR BLOQUE", foreground="#BC0017",font=fuente)
    #     self.titulo_agregar.place(relx=0.05,rely=0.05,relwidth=0.9, relheight=0.2)
        
    #     self.info_letra = Label(self.contenedor_agregar,text="Info", bg="#CCCCCC",font=fuente)
    #     self.info_letra.place(relx=0.1,rely=0.3,relwidth=0.8, relheight=0.1)
        
    #     self.txtNum2=Entry(self.contenedor_agregar,bg="#CCCCCC")
    #     self.txtNum2.place(relx=0.10,rely=0.45,relwidth=0.8, relheight=0.05) 
        
    #     self.info_piso = Label(self.contenedor_agregar,text="Info", bg="#CCCCCC",font=fuente)
    #     self.info_piso.place(relx=0.1,rely=0.6,relwidth=0.8, relheight=0.1)

    #     self.txtNum2=Entry(self.contenedor_agregar,bg="#CCCCCC")
    #     self.txtNum2.place(relx=0.1,rely=0.75,relwidth=0.8, relheight=0.05)

    #     self.btnBloques=Button(self.contenedor_agregar,text=" Guardar",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w")
    #     self.btnBloques.place(relx=0.8,rely=0.9,relwidth=0.1, relheight=0.08)


 
    # def validacionCliente(self):
    #         self.contenedor3.destroy()
    #         self.btn_agregar.destroy()


    #         fuente ="Verdana"

    #         self.contenedorCliente = Label(self.fondoBarraDeContenido, bg="#EEEEEE")
    #         self.contenedorCliente.place(relx=0.2,rely=0.3,relwidth=0.6, relheight=0.4)

    #         self.msgConnfirmacion = barraSalida= Label(self.contenedorCliente,text="¿Esta seguro que desea eliminar el registro?", font=fuente)
    #         self.msgConnfirmacion.place(relx=0.2,rely=0.2,relwidth=0.6, relheight=0.2)

    #         self.btnSi=Button(self.contenedorCliente,text=" SI ",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat")
    #         self.btnSi.place(relx=0.2,rely=0.6,relwidth=0.2, relheight=0.2)

    #         self.btnNo=Button(self.contenedorCliente,text=" NO ",  bg="#BC0017", foreground="#FFFFFF", font=fuente, relief="flat",command=lambda: tipos_bloques.contenido(self,self.fondoBarraDeContenido) )
    #         self.btnNo.place(relx=0.6,rely=0.6,relwidth=0.2, relheight=0.2)

    # def agregar(self):
    #     tipos_bloques.contenido(self, self.fondoBarraDeContenido)
    #     #Metodo para consumir servicio de agregar bloques
