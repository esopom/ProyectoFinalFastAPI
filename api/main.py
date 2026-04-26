from fastapi import FastAPI

from api.routes.laptops import router as laptops_router

app = FastAPI(title="API Portatiles")

app.include_router(laptops_router)


@app.get("/")
async def healthcheck():
	return {"message": "API de portatiles activa"}
