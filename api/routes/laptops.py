from fastapi import APIRouter, HTTPException, Path, Query

from api.data.portatildata import PortatilData
from api.utilidades.models import Portatil

router = APIRouter(prefix="/laptops")
portatil_data = PortatilData()


@router.get(
    "/",
    summary="Listar portátiles",
    description="Devuelve una lista de portátiles con paginación opcional y filtro por nombre de modelo.",
)
async def get_laptops(
    skip: int = 0,
    total: int = 50,
    modelo: str | None = Query(None, alias="filtroNombre", description="Filtra los portátiles por el nombre del modelo."),
):
    return await portatil_data.get_portatilesModelo(skip=skip, total=total, filtronombre=modelo)


@router.get(
    "/{laptop_id}",
    summary="Obtener un portátil por id",
    description="Busca un portátil concreto a partir de su identificador.",
)
async def get_laptop(laptop_id: int):
    laptop = await portatil_data.get_portatil(portatil_id=laptop_id)
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return laptop


@router.post(
    "/",
    status_code=201,
    summary="Crear un portátil",
    description="Guarda un nuevo portátil en el archivo de datos.",
)
async def create_laptop(laptop: Portatil):
    return await portatil_data.write_portatil(portatil=laptop)


@router.put(
    "/{laptop_id}",
    summary="Actualizar un portátil",
    description="Actualiza los datos de un portátil existente a partir de su identificador.",
)
async def update_laptop(laptop_id: int, laptop: Portatil):
    updated = await portatil_data.update_portatil(portatil_id=laptop_id, portatil=laptop)
    if updated is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return updated


@router.delete(
    "/{laptop_id}",
    summary="Eliminar un portátil",
    description="Elimina un portátil existente a partir de su identificador.",
)
async def delete_laptop(laptop_id: int):
    deleted = await portatil_data.delete_portatil(portatil_id=laptop_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return deleted

@router.get(
    "/os/{so_portatil}",
    summary="Filtrar portátiles por sistema operativo",
    description="Devuelve los portátiles que coinciden con el sistema operativo indicado.",
)
async def get_portatiles_os(
    so_portatil: str = Path(..., description="Sistema operativo usado para filtrar los portátiles."),
):
    return await portatil_data.get_portatilesOS(os=so_portatil)

@router.get(
    "/precio-max/{precio_max}",
    summary="Filtrar portátiles por precio máximo",
    description="Devuelve los portátiles cuyo precio es menor o igual que el valor indicado.",
)
async def get_portatiles_precio_max(
    precio_max: int = Path(..., description="Precio máximo permitido para devolver portátiles."),
):
    return await portatil_data.get_portatilesPrecioMax(precioMax=precio_max)
