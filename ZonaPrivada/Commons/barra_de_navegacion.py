from tkinter import PhotoImage, Tk,Frame,Label,Button, font,Entry
from prueba import prueba

class barra_de_navegacion (Frame):
    

    def navegacion(self,barraLateral,fondoBarraDeContenido):
        

        print("llego a la barra lateral")
        fuente ="Verdana"

        #command= lambda: prueba.argregarBloque(self,fondoBarraDeContenido )

        self.contenedor0 = Label(barraLateral,text="contenedor1", bg="red", font=fuente)
        self.contenedor0.place(relx=0.1,rely=0.02,relwidth=0.8, relheight=0.05)
        self.btnBloques=Button(self.contenedor0,text="Bloques", bg="#FFFFFF", font=fuente, relief="flat", anchor="w", command =lambda: prueba.contenido(self,fondoBarraDeContenido))
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
