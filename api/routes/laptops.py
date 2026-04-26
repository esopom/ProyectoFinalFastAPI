from fastapi import APIRouter, HTTPException

from api.data.portatildata import PortatilData
from api.utilidades.models import Portatil

router = APIRouter(prefix="/laptops", tags=["laptops"])
portatil_data = PortatilData()


@router.get("/")
async def get_laptops(skip: int = 0, total: int = 50, modelo: str | None = None):
    return await portatil_data.get_portatilesModelo(skip=skip, total=total, filtronombre=modelo)


@router.get("/{laptop_id}")
async def get_laptop(laptop_id: int):
    laptop = await portatil_data.get_portatil(portatil_id=laptop_id)
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return laptop


@router.post("/", status_code=201)
async def create_laptop(laptop: Portatil):
    return await portatil_data.write_portatil(portatil=laptop)


@router.put("/{laptop_id}")
async def update_laptop(laptop_id: int, laptop: Portatil):
    updated = await portatil_data.update_portatil(portatil_id=laptop_id, portatil=laptop)
    if updated is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return updated


@router.delete("/{laptop_id}")
async def delete_laptop(laptop_id: int):
    deleted = await portatil_data.delete_portatil(portatil_id=laptop_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return deleted

@router.get("/os/{so_portatil}")
async def get_portatiles_os(so_portatil: str):
    return await portatil_data.get_portatilesOS(os=so_portatil)

@router.get("/precio-max/{precio_max}")
async def get_portatiles_precio_max(precio_max: int):
    return await portatil_data.get_portatilesPrecioMax(precioMax=precio_max)
