from shutil import which
from tkinter import PhotoImage, Tk,Frame,Label,Button, font,Entry,filedialog
import requests
import json

class digitalizar (Frame):

    def contenido(self,fondoBarraDeContenido):
        fuente ="Verdana"
        fondoBarraDeContenido = self.fondoBarraDeContenido
       
        
        self.contenedor3 = Label(self.fondoBarraDeContenido,text="TMP: CONTENEDOR DE DIGITALIZACION DE IMAGENES", bg="#EEEEEE")
        self.contenedor3.place(relx=0.1,rely=0.1,relwidth=0.8, relheight=0.8)


        self.titulo = Label(self.contenedor3,text="DIGITALIZACION DE DOCUMENTOS", font=fuente)
        self.titulo.place(relx=0.3,rely=0.1,relwidth=0.4, relheight=0.05)

        self.lblNum2 = Label(self.contenedor3,text="Nombre del documento", font=fuente)
        self.lblNum2.place(relx=0.1,rely=0.2,relwidth=0.4, relheight=0.05)
        
        self.txtNum2=Entry(self.contenedor3,bg="#CCCCCC", font=fuente)
        self.txtNum2.place(relx=0.4,rely=0.2,relwidth=0.4, relheight=0.05)

        self.btn_agregar=Button(self.contenedor3,text=" + abir archivo",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w", command= lambda: digitalizar.abir_archivo(self))
        self.btn_agregar.place(relx=0.1,rely=0.3,relwidth=0.2, relheight=0.2)
        
        self.lblNum3 = Label(self.contenedor3,text="Nombre de la pagina", font=fuente)
        self.lblNum3.place(relx=0.4,rely=0.3,relwidth=0.4, relheight=0.05)

        self.txtNum4=Entry(self.contenedor3,bg="#CCCCCC", font=fuente)
        self.txtNum4.place(relx=0.4,rely=0.4,relwidth=0.4, relheight=0.05)



        self.btn_agregar=Button(self.contenedor3,text=" + abir archivo",  bg="#53BF9D", foreground="#FFFFFF", font=fuente, relief="flat", anchor="w", command= lambda: digitalizar.abir_archivo(self))
        self.btn_agregar.place(relx=0.1,rely=0.6,relwidth=0.2, relheight=0.2)
        
        self.lblNum5 = Label(self.contenedor3,text="Nombre de la pagina", font=fuente)
        self.lblNum5.place(relx=0.4,rely=0.6,relwidth=0.4, relheight=0.05)

        self.txtNum6=Entry(self.contenedor3,bg="#CCCCCC", font=fuente)
        self.txtNum6.place(relx=0.4,rely=0.7,relwidth=0.4, relheight=0.05)




    def abir_archivo(self):
        archivo = filedialog.askopenfilename(title="Archivo", initialdir="C:/Users/leyner.ortega_pragma/Documents/[LEYNER]/UFPS/Secretaria/Documentos digitalizados")
        print(archivo)

      