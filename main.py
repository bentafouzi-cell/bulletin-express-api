from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- NOUVEAU : Pour autoriser le frontend
from pydantic import BaseModel
from typing import List
from calculs import calculer_moyenne_generale

app = FastAPI(title="Bulletin Express API")

# <-- NOUVEAU : On autorise toutes les origines (pour le développement)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Composante(BaseModel):
    note: float

class Matiere(BaseModel):
    nom: str
    coefficient_unite: int
    composantes: List[Composante]

class EleveRequest(BaseModel):
    nom: str
    matieres: List[Matiere]

@app.post("/api/calculer")
def calculer_bulletin(donnees: EleveRequest):
    matieres_dict = [m.model_dump() for m in donnees.matieres]
    moyenne, details = calculer_moyenne_generale(matieres_dict)
    
    return {
        "eleve": donnees.nom,
        "moyenne_generale": moyenne,
        "details": details
    }
