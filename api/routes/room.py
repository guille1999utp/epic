from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.main import Room, RoomCreate, RoomUpdate
from controllers.room import get_room, create_room, get_rooms, update_room, delete_room
from database.main import get_db

router = APIRouter()

@router.post("/", response_model=Room)
def create_room_endpoint(room: RoomCreate, db: Session = Depends(get_db)):
    try:
        db_room = create_room(db, room)
        return db_room
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{room_id}", response_model=Room)
def read_room_endpoint(room_id: int, db: Session = Depends(get_db)):
    db_room = get_room(db, room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

@router.get("/", response_model=list[Room])
def read_rooms_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rooms = get_rooms(db, skip=skip, limit=limit)
    return rooms

@router.put("/{room_id}", response_model=Room)
def update_room_endpoint(room_id: int, room: RoomUpdate, db: Session = Depends(get_db)):
    return update_room(db, room_id, room)

@router.delete("/{room_id}", response_model=Room)
def delete_room_endpoint(room_id: int, db: Session = Depends(get_db)):
    return delete_room(db, room_id)