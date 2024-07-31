from sqlalchemy.orm import Session
from models.reservation import Reservation
from schemas.main import ReservationCreate, ReservationUpdate
from models.room import Room
from fastapi import HTTPException

# Reservations
def get_reservation(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def get_reservations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reservation).offset(skip).limit(limit).all()

def create_reservation(db: Session, reservation: ReservationCreate):
    # Verificar si la habitación existe
    room = db.query(Room).filter(Room.id == reservation.room_id).first()
    if room is None:
        raise ValueError("Room does not exist")
    
    # Verificar si la habitación está disponible
    if not room.is_available:
        raise ValueError("Room is not available")

    # Verificar si hay reservas existentes en el rango de fechas
    overlapping_reservations = db.query(Reservation).filter(
        Reservation.room_id == reservation.room_id,
        Reservation.start_date <= reservation.end_date,
        Reservation.end_date >= reservation.start_date
    ).all()


    if overlapping_reservations:
        raise ValueError("Room is already reserved for the selected dates")

    # Crear la reserva
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def update_reservation(db: Session, reservation_id: int, reservation: ReservationUpdate):
    # Obtener la reserva existente
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    
    # Verificar si la reserva existe
    if db_reservation is None:
        raise ValueError("Reservation does not exist")

    # Verificar la validez del room_id, si se ha actualizado
    if reservation.room_id is not None and reservation.room_id != db_reservation.room_id:
        room = db.query(Room).filter(Room.id == reservation.room_id).first()
        if room is None or not room.is_available:
            raise ValueError("Room does not exist or is not available")

    # Actualizar la reserva
    for key, value in reservation.dict().items():
        setattr(db_reservation, key, value)
    
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def delete_reservation(db: Session, reservation_id: int):
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    
    db.delete(db_reservation)
    db.commit()
    return db_reservation