from pydantic import BaseModel, Field
from datetime import date
from typing import Optional,Literal

class RoomBase(BaseModel):
    number: str
    type: Literal['simple', 'doble', 'suite']
    price_per_night: float
    is_available: bool = True

class RoomCreate(RoomBase):
    pass

class RoomUpdate(RoomBase):
    pass

class Room(RoomBase):
    id: int

class ReservationBase(BaseModel):
    guest_name: str
    start_date: date
    end_date: date
    room_id: int

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int