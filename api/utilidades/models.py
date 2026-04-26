#importamos desde fastAPI, la clases FastAPI y Response
from typing import Union
from enum import Enum
from pydantic import BaseModel, Field

# Control Enum OS
class TipoOS(str, Enum):
    mac = "mac"
    windows = "windows"

# Modelo para un Laptop
class Portatil(BaseModel):
    modelo: str
    precio : int = 0
    OS : TipoOS
    marcagpu : str =  None
    memoriaram : int = 0


    

