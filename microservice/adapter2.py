import json


class Convertir:

    def __init__(self,temp,time):
        self.Temperatura = temp
        self.tiempo = time
        
    def htmlToJson(self):
        Datos = {
            'Temperatura': self.Temperatura,
            'tiempo': self.tiempo
        }
        convert = json.dumps(Datos)
        return convert            

