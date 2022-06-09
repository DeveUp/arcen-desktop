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
raiz.iconbitmap('Frontend Desarrollo\ZonaPublica\Img\Ico\logoufps.ico')

#Restriccion de cambiar el tamaño de la ventana (fila,columna)
raiz.resizable(True,True)

# INETENTO DE SUBIR IMAGEN (revisar)
#imagen=PhotoImage(file="UFPSIMAGE.png")
#fondo = Label(raiz, image=imagen).place(relx=0.3, rely=0.04)
#fondo.pacck()



#Metodo para que muestre el mensaje desccrito
def salir():
    lb = Label(raiz, text="prueba de btn de salida")
    lb.pack()#Posicionar lo que se creo dentro de la ventana

#BARRA SUPERIOR

imgPrincipal = Label(raiz,text="Imagen ufps", bg="red")
imgPrincipal.place(relx=0,rely=0,relwidth=0.20, relheight=0.10)

nombreDependencia = Label(raiz,text="Auxiliar de dependencia externa", bg="pink")
nombreDependencia.place(relx=0.2,rely=0,relwidth=0.5, relheight=0.10)

barraSalida = nombreDependencia = Label(raiz,text="Barra de salida", bg="yellow")
barraSalida.place(relx=0.7,rely=0,relwidth=0.3, relheight=0.10)

btn=Button(barraSalida,text="SALIR", command=salir)
btn.place(relx=0.6,rely=0.3,relwidth=0.2, relheight=0.8)

#BARRA LATERAL
barraLateral = Label(raiz,text="Negocio", bg="pink")
barraLateral.place(relx=0.0,rely=0.1,relwidth=0.2, relheight=0.9)

#BARRA DE CONTENIDO
barraDeContenido = Label(raiz,text="Inicio", bg="red")
barraDeContenido.place(relx=0.2,rely=0.1,relwidth=0.8, relheight=0.9)

#barraDeRuta = Label(raiz,text="Negocio", bg="white")
#barraDeRuta.place(x=256,y=204.8,width=1024, height=819)



#lblB1 = Label(raiz,text="Bloque 1",bg="yellow")
#lblB1.place(x=350,y=250,width=700, height=60)

#btn=Button(raiz,text="Editar")
#btn.place(relx=1100,y=250,width=50, height=60)

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









#Construir ventana, se corre el ciclo principal de la ventana y se encarga de monitorear la interaccion del usuario con la ventana
raiz.mainloop()