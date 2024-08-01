from fastapi import FastAPI
from database.main import engine, Base
from api.routes import room, reservation
import logging

Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(room.router, prefix="/rooms", tags=["rooms"])
app.include_router(reservation.router, prefix="/reservations", tags=["reservations"])