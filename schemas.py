from pydantic import BaseModel
from typing import List
from enum import Enum


class TypeParcours(str, Enum):
    EXCELLENCE = "Excellence"
    PRIVE = "Ecole privée"
    PUBLIC = "Ecole publique"
    NORMAL = "Classique"


class NiveauEtude(str, Enum):
    BAC = "Bac"
    LICENCE = "Licence"
    MASTER = "Master"
    DOCTORAT = "Doctorat"


class Formation(BaseModel):
    niveau: NiveauEtude
    filiere: str
    ecoles: List[str]
    domaine: str
    description: str | None = None


class Parcours(BaseModel):
    category: TypeParcours
    formations: List[Formation]


class Form(BaseModel):
    niveau_etude: str
    specialite: str | None = None
    matieres: str | None = None
    passions: str | None = None
    metier: str | None = None
