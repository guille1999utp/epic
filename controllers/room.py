from sqlalchemy.orm import Session
from models.room import Room
from schemas.main import RoomCreate, RoomUpdate
from fastapi import HTTPException

def get_room(db: Session, room_id: int):
    return db.query(Room).filter(Room.id == room_id).first()

def get_rooms(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Room).offset(skip).limit(limit).all()

def create_room(db: Session, room: RoomCreate):
    # Verificar si la habitación con el mismo número ya existe
    existing_room = db.query(Room).filter(Room.number == room.number).first()
    if existing_room:
        raise ValueError("Room with this number already exists")

    # Crear la nueva habitación
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def update_room(db: Session, room_id: int, room: RoomUpdate):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    
    # Verificar si el nuevo número ya está en uso por otra habitación
    if db.query(Room).filter(Room.number == room.number, Room.id != room_id).first():
        raise HTTPException(status_code=400, detail="Room number already in use")
    
    for key, value in room.dict().items():
        setattr(db_room, key, value)
    
    db.commit()
    db.refresh(db_room)
    return db_room

def delete_room(db: Session, room_id: int):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    
    db.delete(db_room)
    db.commit()
    return db_room