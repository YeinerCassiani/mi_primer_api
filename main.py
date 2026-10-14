from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

misiones = [
    {
        "id": 1,
        "nombre": "Explorar Marte",
        "destino": "Marte",
        "tripulantes": 4
    },
    {
        "id": 2,
        "nombre": "Estación Lunar",
        "destino": "Luna",
        "tripulantes": 2
    },
    {
            "id": 3,
            "nombre": "Amarte mas no pude",
            "destino": "Marte",
            "tripulantes": 1
    }
]

class Mision(BaseModel):
    nombre: str
    destino: str
    tripulantes: int

@app.get("/")
def inicio():
    return {"mensaje": "Centro de control espacial, bienvenido."}

@app.get("/misiones")
def listar_misiones():
    return misiones

@app.get("/buscar")
def buscar_misiones(destino: str):
    resultados = []

    for mision in misiones:
        if mision["destino"].lower() == destino.lower():
            resultados.append(mision)
    
    return resultados 

@app.post("/misiones")
def crear_mision(mision: Mision):
    nuevo_id = len(misiones) + 1
    nueva_mision = {
        "id": nuevo_id,
        "nombre": mision.nombre,
        "destino": mision.destino,
        "tripulantes": mision.tripulantes
    }

    misiones.append(nueva_mision)

    return nueva_mision
