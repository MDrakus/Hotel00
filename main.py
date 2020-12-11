from db.hotel_db import HotelInDB
from db.hotel_db import update_hotel, get_hotel
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.hotel_models import HotelIn, HotelOut
from models.transaction_models import TransactionIn, TransactionOut
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.post("/hotel/auth/")
async def auth_hotel(hotel_in: HotelIn):

    hotel_in_db = get_hotel(hotel_in.nombre)

    if hotel_in_db == None:
        raise HTTPException(status_code=404, detail="El Hotel no existe")

    if hotel_in_db.ubicacion != hotel_in.ubicacion:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get("/hotel/totalHabitaciones/{nombre}")
async def get_balance(nombre: str):

    hotel_in_db = get_hotel(nombre)

    if hotel_in_db == None:
        raise HTTPException(status_code=404, detail="El Hotel no existe")

    hotel_out = HotelOut(**hotel_in_db.dict())

    return  hotel_out


@api.put("/hotel/transaction/")
async def make_transaction(transaction_in: TransactionIn):

    hotel_in_db = get_hotel(transaction_in.nombre)

    if hotel_in_db == None:
        raise HTTPException(status_code=404, detail="El hotel no existe")

    if hotel_in_db.totalHabitaciones < transaction_in.totalHabitaciones:
        raise HTTPException(status_code=400, detail=" ")

    hotel_in_db.totalHabitaciones = hotel_in_db.totalHabitaciones - transaction_in.reserva
    update_hotel(hotel_in_db)

    transaction_in_db = TransactionInDB(**transaction_in.dict(), totalHabs = hotel_in_db.totalHabitaciones)
    transaction_in_db = save_transaction(transaction_in_db)

    transaction_out = TransactionOut(**transaction_in_db.dict())

    return  transaction_out