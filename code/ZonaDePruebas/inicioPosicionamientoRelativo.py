from re import S
from tkinter import PhotoImage, Tk,Label,Button,Entry


#Clase principal para crear una ventana principal
raiz=Tk()

# Titulo de la ventana
raiz.title("Secretaria general de la UFPS")

# Detectar el tamaño de la pantalla
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
print(screen_width)
print(screen_height)

#Configurar tamaño de ventana, aplicandole el tamaño de la pantalla detectado
#raiz.geometry(1024x980)
raiz.geometry(str(screen_width)+"x"+str(screen_height)) 

# Añadir icono del lado derecho de la ventana con la (Ruta relativa)
raiz.iconbitmap('Frontend Desarrollo\ZonaPublica\Img\Ico')

#Restriccion de cambiar el tamaño de la ventana (fila,columna)
raiz.resizable(True,True)




#padx, padx: Especifican margenes externos
#ipadx, ipadx: Especifican margenes internos
#expand: tiene dos valores True o False con el cual se determina si el espacio que ocupa es todo el tamaño del padre

imgPrincipal = Label(raiz,text="Imagen ufps", bg="red", border=10)

nombreDependencia = Label(raiz,text="Auxiliar de dependencia externa", bg="pink")

btnSalir=Button(raiz,text="SALIR", border=1)

barraLateral = Label(raiz,text="Negocio", bg="pink")

barraDeRuta = Label(raiz,text="Inicio", bg="red")

zonaDeNegocio = Label(raiz,text="Negocio", bg="white")




#lblB1 = Label(raiz,text="Bloque 1",bg="yellow")
#lblB1.place(x=350,y=250,width=700, height=60)

#btn=Button(raiz,text="Editar")
#btn.place(x=1100,y=250,width=50, height=60)

#btn=Button(raiz,text="Eliminar")
#btn.place(x=1160,y=250,width=50, height=60)



#lblB2 = Label(raiz,text="Bloque 2",bg="yellow")
#lblB2.place(x=350,y=350,width=700, height=60)

#btn=Button(raiz,text="Editar")
#btn.place(x=1100,y=350,width=50, height=60)

#btn=Button(raiz,text="Eliminar")
#btn.place(x=1160,y=350,width=50, height=60)


#lblB2 = Label(raiz,text="Bloque 4",bg="yellow")
#lblB2.place(x=350,y=450,width=700, height=60)

#btn=Button(raiz,text="Editar")
#btn.place(x=1100,y=450,width=50, height=60)

#btn=Button(raiz,text="Eliminar")
#btn.place(x=1160,y=450,width=50, height=60)



#lblB2 = Label(raiz,text="Bloque 3",bg="yellow")
#lblB2.place(x=350,y=350,width=700, height=60)

#btn=Button(raiz,text="Editar")
#btn.place(x=1100,y=350,width=50, height=60)

#btn=Button(raiz,text="Eliminar")
#btn.place(x=1160,y=350,width=50, height=60)





#lblB2 = Label(raiz,text="Bloque 5",bg="yellow")
#lblB2.place(x=350,y=550,width=700, height=60)

#btn=Button(raiz,text="Editar")
#btn.place(x=1100,y=550,width=50, height=60)

#btn=Button(raiz,text="Eliminar")
#btn.place(x=1160,y=550,width=50, height=60)






#lblB2 = Label(raiz,text="Bloque 6",bg="yellow")
#lblB2.place(x=350,y=650,width=700, height=60)


#btn=Button(raiz,text="Editar")
#btn.place(x=1100,y=650,width=50, height=60)

#btn=Button(raiz,text="Eliminar")
#btn.place(x=1160,y=650,width=50, height=60)

















imgPrincipal.place(relx=0.00, rely=0.00 , relwidth=0.20, relheight=0.10)
nombreDependencia.place(relx=0.20, rely=0.00 , relwidth=0.50, relheight=0.10)
btnSalir.place(relx=0.70, rely=0.0 , relwidth=0.30, relheight=0.10)
barraLateral.place(relx=0.00, rely=0.10, relwidth=0.20, relheight=0.90)
barraDeRuta.place(relx=0.20, rely=0.10, relwidth=0.80, relheight=0.10)
zonaDeNegocio.place(relx=0.20, rely=0.20, relwidth=0.80, relheight=0.80)

# Configuracion de la posicion de cada uno de los elementos en la ventana
#imgPrincipal.grid(row=0,column=0, columnspan=1,sticky="nsew")
#nombreDependencia.grid(row=1,column=0,sticky="nsew")
#btn.grid(row=1,column=1,sticky="nsew")


#Construir ventana, se corre el ciclo principal de la ventana y se encarga de monitorear la interaccion del usuario con la ventana
raiz.mainloop()