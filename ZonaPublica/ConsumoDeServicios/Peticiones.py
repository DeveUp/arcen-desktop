import urllib, json,requests


class ConsumoDeServicios():

    def obtenerUsuarios(email,documento, contraseña):
        usuarioRs =email.get()

        API= 'https://api.openweathermap.org/data/2.5/weather?q=&appid=f08c20ee319398d4ccb55d6a775da822'  
        try:
		    json_datos = requests.get(API).json()
		    temp['text'] = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
		    temp_min['text'] = str(int(json_datos['main']['temp_min'] - 273.15))  +" °C"
		    temp_max['text'] = str(int(json_datos['main']['temp_max'] - 273.15)) +" °C"
		    presion['text'] = str(json_datos['main']['pressure']) + ' hPa'
		    humedad['text'] = str(json_datos['main']['humidity']) + ' %'	    
		    viento['text'] = str(int(json_datos['wind']['speed'])*18/5) + ' km/h'
		    localidad['text'] =  json_datos['name'] + ' - '+ json_datos['sys']['country'] 
		    print(json_datos)
	    except:
	    	self.aviso['text'] =  'Error'
	    	self.temp['text'] = '-'
	    	self.temp_min['text'] = '-'
	    	self.temp_max['text'] = '-'
	    	self.presion['text'] = '-'
	    	self.humedad['text'] = '-'
	    	self.viento['text'] = '-'
	    	self.master.update()
	    	time.sleep(1)	    	
	    	self.aviso['text'] = ''
	    	self.localidad['text'] = ''


        def obtenerUsuarios(email,documento, contraseña):
        usuarioRs =email.get()

        API= 'https://api.openweathermap.org/data/2.5/weather?q=&appid=f08c20ee319398d4ccb55d6a775da822'  
        try:
		    json_datos = requests.get(API).json()
		    temp['text'] = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
		    temp_min['text'] = str(int(json_datos['main']['temp_min'] - 273.15))  +" °C"
		    temp_max['text'] = str(int(json_datos['main']['temp_max'] - 273.15)) +" °C"
		    presion['text'] = str(json_datos['main']['pressure']) + ' hPa'
		    humedad['text'] = str(json_datos['main']['humidity']) + ' %'	    
		    viento['text'] = str(int(json_datos['wind']['speed'])*18/5) + ' km/h'
		    localidad['text'] =  json_datos['name'] + ' - '+ json_datos['sys']['country'] 
		    print(json_datos)
	    except:
	    	self.aviso['text'] =  'Error'
	    	self.temp['text'] = '-'
	    	self.temp_min['text'] = '-'
	    	self.temp_max['text'] = '-'
	    	self.presion['text'] = '-'
	    	self.humedad['text'] = '-'
	    	self.viento['text'] = '-'
	    	self.master.update()
	    	time.sleep(1)	    	
	    	self.aviso['text'] = ''
	    	self.localidad['text'] = ''

        def obtenerUsuarios(email,documento, contraseña):
        usuarioRs =email.get()

        API= 'https://api.openweathermap.org/data/2.5/weather?q=&appid=f08c20ee319398d4ccb55d6a775da822'  
        try:
		    json_datos = requests.get(API).json()
		    temp['text'] = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
		    temp_min['text'] = str(int(json_datos['main']['temp_min'] - 273.15))  +" °C"
		    temp_max['text'] = str(int(json_datos['main']['temp_max'] - 273.15)) +" °C"
		    presion['text'] = str(json_datos['main']['pressure']) + ' hPa'
		    humedad['text'] = str(json_datos['main']['humidity']) + ' %'	    
		    viento['text'] = str(int(json_datos['wind']['speed'])*18/5) + ' km/h'
		    localidad['text'] =  json_datos['name'] + ' - '+ json_datos['sys']['country'] 
		    print(json_datos)
	    except:
	    	self.aviso['text'] =  'Error'
	    	self.temp['text'] = '-'
	    	self.temp_min['text'] = '-'
	    	self.temp_max['text'] = '-'
	    	self.presion['text'] = '-'
	    	self.humedad['text'] = '-'
	    	self.viento['text'] = '-'
	    	self.master.update()
	    	time.sleep(1)	    	
	    	self.aviso['text'] = ''
	    	self.localidad['text'] = ''

        def obtenerUsuarios(email,documento, contraseña):
        usuarioRs =email.get()

        API= 'https://api.openweathermap.org/data/2.5/weather?q=&appid=f08c20ee319398d4ccb55d6a775da822'  
        try:
		    json_datos = requests.get(API).json()
		    temp['text'] = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
		    temp_min['text'] = str(int(json_datos['main']['temp_min'] - 273.15))  +" °C"
		    temp_max['text'] = str(int(json_datos['main']['temp_max'] - 273.15)) +" °C"
		    presion['text'] = str(json_datos['main']['pressure']) + ' hPa'
		    humedad['text'] = str(json_datos['main']['humidity']) + ' %'	    
		    viento['text'] = str(int(json_datos['wind']['speed'])*18/5) + ' km/h'
		    localidad['text'] =  json_datos['name'] + ' - '+ json_datos['sys']['country'] 
		    print(json_datos)
	    except:
	    	self.aviso['text'] =  'Error'
	    	self.temp['text'] = '-'
	    	self.temp_min['text'] = '-'
	    	self.temp_max['text'] = '-'
	    	self.presion['text'] = '-'
	    	self.humedad['text'] = '-'
	    	self.viento['text'] = '-'
	    	self.master.update()
	    	time.sleep(1)	    	
	    	self.aviso['text'] = ''
	    	self.localidad['text'] = ''



