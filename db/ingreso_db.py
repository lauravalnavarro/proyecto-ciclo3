from pydantic.types import ConstrainedStr
from models import ingreso
from pydantic import BaseModel
from typing import Dict

class IngresoInDB(BaseModel): #IngresoInDB hereda de BaseModel
    id_ingreso: int = 0  #Valor por defecto
    tipo: str
    valor: int
    constante: bool

#Diccionario?? tipos_validos = Dict['salario', 'ocasional', 'inversion']
tipos_validos = ['salario', 'ocasional', 'inversion']

database_ingresos = {
    "salario": IngresoInDB(**{"id_ingreso": 101,
                        "tipo": "salario",
                        "valor": 0,
                        "constante": False}),
    "ocasional": IngresoInDB(**{"id_ingreso": 102,
                        "tipo": "ocasional",
                        "valor": 0,
                        "constante": False}),
    "inversion": IngresoInDB(**{"id_ingreso": 103,
                            "tipo": "inversion",
                            "valor": 0,
                            "constante": False}),

}

#generator no se aumenta
generator = {'id': 102}

#para qué?
print( database_ingresos["salario"].valor)

#no se usa .append?
def save_ingresos(ingreso_in_db: IngresoInDB):
    database_ingresos[ingreso_in_db.tipo].valor = ingreso_in_db.valor

    return ingreso_in_db

def get_ingresos(id: str):
    if id in database_ingresos.keys():
        return database_ingresos[id]
    else: 
        return None

def update_ingresos(ingreso_in_db: IngresoInDB, database_ingresos: dict):
    ingreso_in_db[ingreso_in_db.id_ingreso] = ingreso_in_db
    return ingreso_in_db
