from sqlalchemy import Column, Integer, Float, String
from database.database import Base

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True)
    place = Column(String)
    temperature = Column(Float)
    brightness = Column(String)
    noise = Column(String)
    measured_at = Column(String)