from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from calculs import calculer_moyenne_generale

app = FastAPI(title="Bulletin Express API")

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
    # Convertir les données Pydantic en dictionnaires pour notre fonction
    matieres_dict = [m.model_dump() for m in donnees.matieres]
    
    moyenne, details = calculer_moyenne_generale(matieres_dict)
    
    return {
        "eleve": donnees.nom,
        "moyenne_generale": moyenne,
        "details": details
     # 🚀 Test du trigger automatique pour Bulletin Express !
    }
