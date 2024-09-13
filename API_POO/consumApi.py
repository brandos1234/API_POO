import requests
import json
import pandas as pd
from pandas import json_normalize 

class api_num: 
    
    def __init__(self, url_api, var):
        self.url_api = url_api
        self.var = var
        self.datos = None
      
        
    def consumo(self):
        datos = requests.get(self.url_api)

        if datos.status_code == 200:
            datos_json = self.transformacion(datos)
            return datos_json
        else:
            raise Exception(f'Falló el consumo:{datos.status_code}')

    def transformacion(self, datos):
        datos = json.loads(datos.text)
        datos = json_normalize(datos)
        arreglo = datos[self.var].tolist()
        return arreglo, datos

