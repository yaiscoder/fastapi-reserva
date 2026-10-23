from fastapi import FastAPI
from app.src.presentation.routers.booking_router import router as booking_router

app = FastAPI(
    title="Bookings Service",
    description="Microservicio para gestionar reservas de recursos.",
    version="1.0.0",
)

app.include_router(booking_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "bookings-service"}
