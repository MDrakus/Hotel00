from pydantic import BaseModel

class HotelIn(BaseModel):
    nombre: str
    ubicacion: str

class HotelOut(BaseModel):
    nombre: str
    totalHabitaciones: int
