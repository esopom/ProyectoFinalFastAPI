import json
import os
from api.utilidades.models import Portatil


# Clase que nos permite trabajar con los datos de laptops
class PortatilData:

    #Propiedades que almacenarán todos los datos
    portatiles=[]
    filePortatiles = None
    directorio_trabajo=None

    def __init__(self):
        self.directorio_trabajo = os.getcwd()
        self.directorio_trabajo=self.directorio_trabajo+"\\api\\data\\"
        #Carga de los ficheros de datos de prueba
        self.filePortatiles=open(self.directorio_trabajo+'portatiles.json')
        self.portatiles = json.load(self.filePortatiles)
        self.filePortatiles.close()


    # Devolucion asincrona de un portatil
    async def get_portatil(self,portatil_id: int):
        # si no se encuentra el alimento se devolverá el nulo en vez de un objeto JSON
        portatil=None
        #Recorremos todos los datos JSON
        for item in self.portatiles['portatiles']:
            #Comparamos el id que es int
            if item['id']==portatil_id:
                portatil=item
                break
        return portatil

    # Devolucion asincrona todos los portátiles
    async def get_allPortatiles(self):
        return self.portatiles

    #Devolucion asincrona de datos de portatiles de un modelo
    async def get_portatilesModelo(self,skip:int,total: int,filtronombre=None):
        portatiles=[]
        #si existe filtronombre nos quedamos con aquellos que contengan ese filtro
        if(filtronombre):
            for item in self.portatiles['portatiles'][skip:(total+skip)]:
                # Comparamos el id que es int
                if filtronombre in item['modelo']:
                    portatiles.append(item)
        else:
            portatiles = self.portatiles['portatiles'][skip:(total+skip)]
        return {'portatiles':portatiles}

    # Devolucion asincrona de datos de portatiles con un precio menor al marcado
    async def get_portatilesPrecioMax(self,precioMax: int):
        portatiles=[]
        #si existe filtronombre nos quedamos con aquellos que contengan ese filtro
        for item in self.portatiles['portatiles']:
            # Comparamos el id que es int
            if item['precio']<=precioMax:
                portatiles.append(item)
        return {'portatiles':portatiles}

    # Devolucion asincrona de datos de portatiles por sistema operativo
    async def get_portatilesOS(self,os: str):
        portatiles=[]
        #si existe filtronombre nos quedamos con aquellos que contengan ese filtro
        for item in self.portatiles['portatiles']:
            # Comparamos el id que es int
            if item['OS']==os:
                portatiles.append(item)
        return {'portatiles':portatiles}

    # Recibimos y guardamos un nuevo portatil
    async def write_portatil(self, portatil: Portatil):
        self.filePortatiles=open(self.directorio_trabajo+'portatiles.json', 'w')
        #Conseguimos el último id de la lista
        ultimo_portatil=self.portatiles['portatiles'][-1]['id']
        #Añadimos un nuevo id al ingrediente nuevo
        portatilDict=portatil.model_dump()
        portatilDict['id']=ultimo_portatil+1
        self.portatiles['portatiles'].append(portatilDict)
        json.dump(self.portatiles,self.filePortatiles,indent=2)
        self.filePortatiles.close()
        return portatilDict

    # Recibimos y actualizamos un nuevo ingrediente
    async def update_portatil(self, portatil_id: int, portatil: Portatil):
        self.filePortatiles=open(self.directorio_trabajo+'portatiles.json', 'w')
        #Buscamos el portatil
        portatilEncontrado=None
        portatilPos=0
        #Recorremos todos los datos JSON
        for item in self.portatiles['portatiles']:
            #Comparamos el id que es int
            if item['id']==portatil_id:
                portatilEncontrado=item
                break
            portatilPos=portatilPos+1
        #Si se ha encontrado
        if(portatilEncontrado):
            #Realizamos la actualization
            portatilDict = portatil.model_dump()
            for elem in portatilDict:
                if(portatilDict[elem]):
                #cambiamos el valor
                    self.portatiles['portatiles'][portatilPos][elem]=portatilDict[elem]
            json.dump(self.portatiles,self.filePortatiles,indent=2)
            self.filePortatiles.close()
            return self.portatiles['portatiles'][portatilPos]
        else:
            return None

    # Borramos un portatil
    async def delete_portatil(self, portatil_id: int):
        self.filePortatiles=open(self.directorio_trabajo+'portatiles.json', 'w')
        #Buscamos el portatil
        portatilEncontrado=None
        portatilPos=0
        #Recorremos todos los datos JSON
        for item in self.portatiles['portatiles']:
            #Comparamos el id que es int
            if item['id']==portatil_id:
                portatilEncontrado=item
                break
            portatilPos=portatilPos+1
        #Si se ha encontrado
        if(portatilEncontrado):
            self.portatiles['portatiles'].pop(portatilPos)
            json.dump(self.portatiles,self.filePortatiles,indent=2)
            self.filePortatiles.close()
            return {"info":"borrado portatil "+str(portatil_id)}
        else:
            return None
