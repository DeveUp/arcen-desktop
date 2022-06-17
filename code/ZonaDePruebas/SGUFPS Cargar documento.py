from cgitb import grey
from tkinter import*
from tkinter import filedialog
from tokenize import blank_re

#Para ejecutar la aplicacion como .exe cambiar la extencion del archivo a .pyw


#Clase principal para crear una ventana principal
raiz=Tk()

# Titulo de la ventana
raiz.title("Secretaria general de la UFPS")

#Configurar tamaño (Se deine el tamaño estandar para HD)
raiz.geometry("1280x1024") 

#Añadir icono del lado derecho de la ventana
#raiz.iconbitmap('logoufps.ico')

#Restriccion de cambiar el tamaño de la ventana (fila,columna)
raiz.resizable(True,True)

#Cambiar el color de fondo
raiz.config(background="blue")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Crear textos
lbl = Label(raiz, text="Inicio de sesion texto")
lbl.pack()#Posicionar lo que se creo dentro de la ventana

#Metodo para que muestre el mensaje desccrito
def iniciarSession():
    lb = Label(raiz, text="Se registra intento de inicio de session")
    lb.pack()#Posicionar lo que se creo dentro de la ventana

#Crear botones
btn=Button(raiz,text="Iniciar sesion", command=iniciarSession)
btn.pack()

#Cambiar o ponerle propiedades forma 1
btn.config(fg="red",bg="black")

#Cambiar o ponerle propiedades forma 2
lbl["fg"] = "grey"
lbl["bg"] = "orange"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funcion para cargar archivos
def abrirArchivo():
    archivo = filedialog.askopenfilename(title="Cargar archivo", initialdir="C:/")
    print(archivo)

Button(raiz, text= "Cargar Archivo", command=abrirArchivo).pack()







#Construir ventana, se corre el ciclo principal de la ventana y se encarga de monitorear la interaccion del usuario con la ventana
raiz.mainloop()