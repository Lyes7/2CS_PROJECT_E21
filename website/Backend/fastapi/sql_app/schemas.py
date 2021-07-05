import datetime
from typing import Optional, Set, List
from pydantic import BaseModel


class Membre(BaseModel):
    userID:str
    hashed_password:str
    email:str
    tel:str
    #uuid:str
    is_president:bool = None
    signature:str



class Ordre(BaseModel):
    abv:str
    titre:str
    motif:str
    validation:bool = None


class Conseil(BaseModel):
    nom:str
    president:str
    membres:str
    #uuid:str



class Pv(BaseModel):
    date:datetime.datetime
    conseil:str
    membresPresent:str
    ordres:str
    #uuid: str

class Reunion(BaseModel):
    date:datetime.datetime
    conseil:str
    ordres:str
    #uuid: str

class ReunionCreation(BaseModel):
    date: Optional[str] = None
    conseil:Optional[str] = None
    o1: Optional[str] = None
    o2: Optional[str] = None
    o3: Optional[str] = None
    o4: Optional[str] = None
    #uuid: str

class Proposition(BaseModel):
    titre:str
    validation:bool = None
    #uuid: str

class Doctorant(BaseModel):
    nom:str
    prenom:str
    propositions:str
    #uuid: str

class Decrit(BaseModel):
    numero:int
    description:str
    date: str
    #uuid: str


