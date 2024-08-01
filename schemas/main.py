from pydantic import BaseModel, Field, validator
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
   
    # Validador que se encarga de la fecha de inicio sea menor a la fecha de fin
    @validator('end_date')
    def end_date_must_be_after_start_date(cls, end_date, values):
        start_date = values.get('start_date')
        if start_date and end_date < start_date:
            raise ValueError('End date must be after start date')
        return end_date

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int