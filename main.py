import fastapi
from db.ingreso_db import IngresoInDB
from db.ingreso_db import save_ingresos, get_ingresos, update_ingresos
from models.ingreso import IngresoIn, IngresoOut

from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@api.put("/user/ingresos/")
async def make_ingreso(ingreso: IngresoIn):
    ingreso_in_db = IngresoInDB(**ingreso.dict())
    ingreso_in_db = save_ingresos(ingreso_in_db)
    salida =  IngresoOut(**ingreso_in_db.dict())
    return salida

@api.get("/user/ingresos/{id_ingreso}")
async def get_ingresos_main(id_ingreso: str):
    ingreso_in_db = get_ingresos(id_ingreso)
    if ingreso_in_db == None:
        raise HTTPException(status_code=404,
                            detail= "El id no existe")
    ingreso_out = IngresoOut(**ingreso_in_db.dict())
    return ingreso_out