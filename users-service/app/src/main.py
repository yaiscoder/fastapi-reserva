from fastapi import FastAPI
from app.src.presentation.routers.user_router import router as user_router


app = FastAPI(
    title="Users Service",
    description="Microservicio de gestión de usuarios",
    version="1.0.0",
)

app.include_router(user_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
