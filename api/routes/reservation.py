from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.main import Reservation, ReservationUpdate, ReservationCreate
from controllers.reservation import get_reservation, create_reservation, get_reservations, update_reservation, delete_reservation
from database.main import get_db

router = APIRouter()

@router.post("/", response_model=Reservation)
def create_reservation_endpoint(reservation: ReservationCreate, db: Session = Depends(get_db)):
    try:
        db_reservation = create_reservation(db, reservation)
        return db_reservation
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{reservation_id}", response_model=Reservation)
def read_reservation_endpoint(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = get_reservation(db, reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation

@router.get("/", response_model=list[Reservation])
def read_reservations_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reservations = get_reservations(db, skip=skip, limit=limit)
    return reservations

@router.put("/{reservation_id}", response_model=Reservation)
def update_reservation_endpoint(reservation_id: int, reservation: ReservationUpdate, db: Session = Depends(get_db)):
    try:
        db_reservation = update_reservation(db, reservation_id, reservation)
        return db_reservation
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{reservation_id}", response_model=Reservation)
def delete_reservation_endpoint(reservation_id: int, db: Session = Depends(get_db)):
    return delete_reservation(db, reservation_id)