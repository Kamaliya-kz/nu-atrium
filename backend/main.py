from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from function import get_temperature_recommendation
from function import study_score
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
def get_readings():

    db = SessionLocal()

    readings = db.query(Reading).all()
    db.execute("""CREATE TABLE NU-Atrium(
               id integer,
               place text,
               temperature float,
               brightness text,
               noise text
               )
               """)
    result = []

    for reading in readings:
        result.append(
            {
                "id": reading.id,
                "place": reading.place,
                "temperature": reading.temperature,
                "brightness": reading.brightness,
                "noise": reading.noise,
                "measured_at": reading.measured_at,
            }
        )

    
    db.commit()

    db.close()
     

    return result