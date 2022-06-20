from cProfile import label
from tkinter import PhotoImage, Tk,Frame,Label,Button, font,Entry
from bloques import bloques
#from bloques import bloques

class barra_de_navegacion (Frame):
    

    def navegacion(self,barraLateral,fondoBarraDeContenido):
        

        print("llego a la barra lateral")
        fuente ="Verdana"

     
        # BLOQUES
        self.contenedor0 = Label(barraLateral,text="contenedor1", bg="#EEEEEE", font=fuente)
        self.contenedor0.place(relx=0.1,rely=0.02,relwidth=0.8, relheight=0.15)
        
        self.btnBloques=Label(self.contenedor0,text="BLOQUES", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=0.33)

        self.btnBloques=Button(self.contenedor0,text="   › Bloques", bg="#FFFFFF", font=fuente, relief="flat", anchor="w", command =lambda: bloques.contenido(self,fondoBarraDeContenido))
        self.btnBloques.place(relx=0.0,rely=0.333,relwidth=1, relheight=0.33)
        
        self.btnBloques=Button(self.contenedor0,text="   › Tipos de bloques", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.666,relwidth=1, relheight=0.33)

        #MUEBLES
        self.contenedor1 = Label(barraLateral,text="contenedor1", bg="#EEEEEE", font=fuente)
        self.contenedor1.place(relx=0.1,rely=0.16,relwidth=0.8, relheight=0.15)
        
        self.btnBloques=Label(self.contenedor1,text="MUEBLES", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=0.33)

        self.btnBloques=Button(self.contenedor1,text="   › Muebles", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.333,relwidth=1, relheight=0.33)

        self.btnBloques=Button(self.contenedor1,text="   › Tipos de muebles", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.666,relwidth=1, relheight=0.33)



        #ESTANTES
        self.contenedor2 = Label(barraLateral,text="contenedor1", bg="#EEEEEE", font=fuente)
        self.contenedor2.place(relx=0.1,rely=0.3,relwidth=0.8, relheight=0.15)
        
        self.btnBloques=Label(self.contenedor2,text="ESTANTES", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=0.33)

        self.btnBloques=Button(self.contenedor2,text="   › Estantes", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.333,relwidth=1, relheight=0.33)

        self.btnBloques=Button(self.contenedor2,text="   › Tipos de estantes", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.666,relwidth=1, relheight=0.33)

        #CAJAS
        self.contenedor3 = Label(barraLateral,text="contenedor1", bg="#EEEEEE", font=fuente)
        self.contenedor3.place(relx=0.1,rely=0.44,relwidth=0.8, relheight=0.15)
        
        self.btnBloques=Label(self.contenedor3,text="CAJAS", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.0,relwidth=1, relheight=0.33)

        self.btnBloques=Button(self.contenedor3,text="   › Cajas", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.333,relwidth=1, relheight=0.33)

        self.btnBloques=Button(self.contenedor3,text="   › Tipos de cajas", bg="#FFFFFF", font=fuente, relief="flat", anchor="w")
        self.btnBloques.place(relx=0.0,rely=0.666,relwidth=1, relheight=0.33)
