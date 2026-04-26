from fastapi import FastAPI

from api.routes.laptops import router as laptops_router

app = FastAPI(
	title="API Portatiles",
	description="Vamos a hacer un repaso de todo el curso para poner en práctica todos nuestros conocimientos, que son muchos y muy interesantes.",
	version="1.0",
	contact="tomasadrian876@gmail.com",
	license_info="Proprietary",
	openapi_tags=[
		{
			"name": "laptops",
			"description": "Operaciones para consultar, crear, actualizar y eliminar portátiles.",
		}
	],
)

app.include_router(laptops_router, tags=["laptops"])


@app.get("/")
async def healthcheck():
	return {"message": "API de portatiles activa"}
