#importamos desde fastAPI, la clases FastAPI y Response
from typing import Union
from enum import Enum
from pydantic import BaseModel, Field


# Modelo para un Laptop
class Portatil(BaseModel):
    modelo: str
    precio : int = 0
    OS : str = None


