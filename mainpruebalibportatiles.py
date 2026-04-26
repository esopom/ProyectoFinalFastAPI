#No es necesario para el proyecto con fastapi
import asyncio
#La importación de la librería variará al construir un proyecto con paquetes Python
from api.data.portatildata import PortatilData
from api.utilidades.models import Portatil

# Ejemplo de uso de librería portatildata
async def main():
    # Se debe crearun objeto Portatildata
    portatiles = PortatilData()

    #LECTURA Y FILTRADO
    #Devolución de un portatil
    resultado=await portatiles.get_portatil(portatil_id=33)
    print(resultado)
    resultado=await portatiles.get_portatil(portatil_id=333333)
    print(resultado)
    #Devolución de todos los portátiles
    resultado=await portatiles.get_allPortatiles()
    print("Número de portátiles devueltos {}".format(len(resultado['portatiles'])))
    #Búsqueda de portatiles desde un inicio(skip) y un total de portatiles(total)
    resultado=await portatiles.get_portatilesModelo(skip=0, total=5)
    print("Número de portátiles devueltos {}".format(len(resultado['portatiles'])))
    #Búsqueda de portatiles desde un inicio(skip) y un total de portatiles(total Max) con texto libre dentro de modelo
    resultado=await portatiles.get_portatilesModelo(skip=0, total=50,filtronombre="Apple")
    print("Número de portátiles devueltos {}".format(len(resultado['portatiles'])))
    #Búsqueda de portatiles con un precio máximo
    resultado=await portatiles.get_portatilesPrecioMax(precioMax=500)
    print("Número de portátiles devueltos {}".format(len(resultado['portatiles'])))
    #Búsqueda de portatiles con un sistema operativo en concreto
    resultado=await portatiles.get_portatilesOS(os="mac")
    print("Número de portátiles devueltos {}".format(len(resultado['portatiles'])))

    # ESCRITURA Y ACTUALIZACIÓN
    portatil1 = Portatil(modelo="Esta es una prueba de un portatil")
    resultado=await portatiles.write_portatil(portatil=portatil1)
    print(resultado)
    portatil2 = Portatil(modelo="Esta es una actualización del portatil de prueba")
    resultado=await portatiles.update_portatil(portatil_id=1003, portatil=portatil2)
    print(resultado)

    # BORRADO
    resultado=await portatiles.delete_portatil(portatil_id=1003)
    print(resultado)

asyncio.run(main())
