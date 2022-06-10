from msilib.schema import RadioButton
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




#Metodo para que muestre el mensaje desccrito
def salir():
    lb = Label(raiz, text="prueba de btn de salida")
    lb.pack()#Posicionar lo que se creo dentro de la ventana

#BARRA SUPERIOR

imgPrincipal = Label(raiz,text="Imagen ufps", bg="#06283D")
imgPrincipal.place(relx=0,rely=0,relwidth=0.20, relheight=0.10)
imgPrincipal.config(cursor="heart", relief="flat")

nombreDependencia = Label(raiz,text="Auxiliar de dependencia externa", bg="pink")
nombreDependencia.place(relx=0.2,rely=0,relwidth=0.5, relheight=0.10)

barraSalida = nombreDependencia = Label(raiz,text="Barra de salida", bg="yellow")
barraSalida.place(relx=0.7,rely=0,relwidth=0.3, relheight=0.10)

btnSalir=Button(barraSalida,text="SALIR", command=salir)
btnSalir.place(relx=0.8,rely=0.1,relwidth=0.1, relheight=0.8,)

usuario = nombreDependencia = Label(barraSalida,text="Leyner Ortega", bg="pink")
usuario.place(relx=0.1,rely=0.1,relwidth=0.6, relheight=0.80)

#BARRA LATERAL
barraLateral = Label(raiz,text="Negocio", bg="pink")
barraLateral.place(relx=0.0,rely=0.1,relwidth=0.2, relheight=0.9)

#BARRA DE CONTENIDO
barraDeContenido = Label(raiz,text="Inicio", bg="red")
barraDeContenido.place(relx=0.2,rely=0.1,relwidth=0.8, relheight=0.9)



#Construir ventana, se corre el ciclo principal de la ventana y se encarga de monitorear la interaccion del usuario con la ventana
raiz.mainloop()