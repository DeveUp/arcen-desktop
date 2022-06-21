from urllib import response
import requests
import json
from tkinter import Frame

class prueba (Frame):
#class bloques (Frame):
    def __init__(self):
        self.email=False
        self.documento=False
        self.contraseña=False

    def peticionPOST(email,documento, contraseña):
        print(email)
        #print(documento)
        #print(contraseña)
        url = "http://httpbin.org/post"
        login_request ={'email':email,'documento':documento, 'contraseña':contraseña}

        response = requests.post(url,data=json.dumps(login_request))

        print(response.email)
        
