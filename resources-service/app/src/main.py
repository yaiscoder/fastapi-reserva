from fastapi import FastAPI
from app.src.presentation.routers.resource_router import router as resource_router

app = FastAPI(
    title="Resources Service",
    description="Microservicio para gestionar recursos reservables",
    version="1.0.0",
)

app.include_router(resource_router)


@app.get("/", tags=["Health"])
def health_check():
    return {"message": "Resources Service funcionando correctamente"}
