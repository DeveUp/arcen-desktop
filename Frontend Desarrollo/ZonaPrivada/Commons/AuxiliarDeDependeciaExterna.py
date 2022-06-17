from tkinter import *
from ContenedoresBase import *
#from Commons.ContenedoresBase import *
#from ZonaPrivada.Commons.ContenedoresBase import ContenedoresBase

def AuxiliarDeDependenciaExterna(self):
    app = self.ContenedoresBase()

    self.contenedor2 = Label(self.ContenedoresBase,text="contenzzzzzzzzzzzz", bg="red")
    self.contenedor2.place(relx=0.1,rely=0.3,relwidth=0.2, relheight=0.05)