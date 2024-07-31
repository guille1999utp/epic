from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.main import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    guest_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    room_id = Column(Integer, ForeignKey("rooms.id"))

    room = relationship("Room", back_populates="reservations")