from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import asc, desc

from database.database import SessionLocal
from database.models import Reading

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.get("/api/readings")
def get_readings(sort: str = "temp_desc"):
    db = SessionLocal()

    query = db.query(Reading)

    if sort == "temp_desc":
        query = query.order_by(desc(Reading.temperature))
    elif sort == "temp_asc":
        query = query.order_by(asc(Reading.temperature))

    readings = query.all()

    result = [
        {
            "id": r.id,
            "place": r.place,
            "temperature": r.temperature,
            "brightness": r.brightness,
            "noise": r.noise,
            "measured_at": r.measured_at,
        }
        for r in readings
    ]

    db.close()
    return result