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
imagen=PhotoImage(file="Frontend Desarrollo\ZonaPublica\Img\img\secrtaria.png")
fondo = Label(raiz, image=imagen)
fondo.pack()

#l = PhotoImage(file = '..\UFPSIMAGE.png')
#label_img = Label(raiz, image = l)
#label_img.pack()


#Metodo para que muestre el mensaje desccrito
def iniciarSession():
    lb = Label(raiz, text="Se registra intento de inicio de session")
    lb.pack()#Posicionar lo que se creo dentro de la ventana




fondoLogin = Label(raiz, bg="white")
fondoLogin.place(relx=0.65,rely=0.15,relwidth=0.3, relheight=0.7)

imgSecundaria = Label(raiz,text="Imagen ufps", bg="red")
imgSecundaria.place(relx=0.70,rely=0.20,relwidth=0.2, relheight=0.1)

lblNum1 = Label(raiz,text="Email",bg="yellow")
lblNum1.place(relx=0.70,rely=0.35,relwidth=0.2, relheight=0.05)
txtNum1=Entry(raiz,bg="pink")
txtNum1.place(relx=0.70,rely=0.4,relwidth=0.2, relheight=0.05)

lblNum2 = Label(raiz,text="Documento",bg="yellow")
lblNum2.place(relx=0.70,rely=0.45,relwidth=0.2, relheight=0.05)
txtNum2=Entry(raiz,bg="pink")
txtNum2.place(relx=0.70,rely=0.5,relwidth=0.2, relheight=0.05)


lblNum3 = Label(raiz,text="Contraseña",bg="yellow")
lblNum3.place(relx=0.70,rely=0.55,relwidth=0.2, relheight=0.05)
txtNum2=Entry(raiz,bg="pink")
txtNum2.place(relx=0.70,rely=0.6,relwidth=0.2, relheight=0.05)




#Crear botones
btn=Button(raiz,text="Iniciar sesion", command=iniciarSession)
btn.place(relx=0.70,rely=0.7,relwidth=0.2, relheight=0.05)


#Construir ventana, se corre el ciclo principal de la ventana y se encarga de monitorear la interaccion del usuario con la ventana
raiz.mainloop()