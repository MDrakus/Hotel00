from typing import  Dict
from pydantic import BaseModel

class HotelInDB(BaseModel):
    nombre:str
    ubicacion:str
    estrellas:str
    totalHabitaciones:int
    sencilla:int
    precioMinSenc:int
    doble:int
    precioMinDob:int
    triple:int
    precioMinTrip:int
    suite:int
    precioMinSuite:int

database_hotels = Dict[str, HotelInDB]

database_hotels = {

    "Hotel1": HotelInDB(**{"nombre":"Hotel1",
                            "ubicacion":"Colombia",
                            "estrellas":"tres",
                            "totalHabitaciones":30,
                            "sencilla":15,
                            "precioMinSenc":70000,
                            "doble":10,
                            "precioMinDob":100000,
                            "triple":3,
                            "precioMinTrip":130000,
                            "suite":2,   
                            "precioMinSuite":200000,            
                                            }),

    "Hotel2": HotelInDB(**{"nombre":"Hotel2",
                            "ubicacion":"Colombia",
                            "estrellas":"dos",
                            "totalHabitaciones":12,
                            "sencilla":4,
                            "precioMinSenc":45000,
                            "doble":4,
                            "precioMinDob":75000,
                            "triple":4,
                            "precioMinTrip":110000,
                            "suite":0,   
                            "precioMinSuite":0,            
                                            }),

    "Hotel3": HotelInDB(**{"nombre":"Hotel3",
                            "ubicacion":"Colombia",
                            "estrellas":"cinco",
                            "totalHabitaciones":40,
                            "sencilla":15,
                            "precioMinSenc":150000,
                            "doble":15,
                            "precioMinDob":250000,
                            "triple":5,
                            "precioMinTrip":320000,
                            "suite":5,   
                            "precioMinSuite":450000,            
                                            }),
}

def get_hotel(nombre: str):
    if nombre in database_hotels.keys():
        return database_hotels[nombre]
    else:
        return None

def update_hotel(hotel_in_db: HotelInDB):
    database_hotels[hotel_in_db.nombre] = hotel_in_db
    return hotel_in_db
