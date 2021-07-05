import datetime
import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Boolean, Integer, String
from uuid import UUID
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import DateTime
from .database import Base

class Membre(Base):
    __tablename__ ="membres"
    id =Column(Integer,primary_key=True, index=True)
    userID = Column(String, unique=True, index= True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index= True)
    tel = Column(String, unique=True, index= True)
    signature=Column(String, index= True)
    is_president = Column(Boolean, default=False)
    uuid=Column(String, unique=True)

class Pv(Base):
    __tablename__ ="pvs"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    ordres = Column(String, index=True)
    membres= Column(String, index=True)
    uuid = Column(String, unique=True)

class Reunion(Base):
    __tablename__ ="reunions"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime,index=True)
    conseil = Column(String, index=True)
    ordres = Column(String, index=True)
    uuid = Column(String, unique=True)


class Proposition(Base):
    __tablename__ ="propositions"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    validation = Column(Boolean, default=False)
    uuid = Column(String, unique=True)

class ordre(Base):
    __tablename__ ="ordres"
    id = Column(Integer, primary_key=True, index=True)
    abv = Column(String, index=True)
    titre = Column(String, index=True)
    validation = Column(Boolean, default=False)
    motif = Column(String, index=True)
    uuid = Column(String, unique=True)

class Doctorant(Base):
    __tablename__ ="doctorants"
    id = Column(Integer, primary_key=True, index=True)
    nom =Column(String, unique=False, index=True)
    prenom = Column(String, unique=False, index=True)
    propositions = Column(String, index=True)
    uuid = Column(String, unique=True)

class Decrit(Base):
    __tablename__ ="decrits"
    id = Column(Integer, primary_key=True, index=True)
    numero=Column(Integer, unique=False, index=True)
    description=Column(String, unique=True, index=True)
    date=Column(String,  index=True)
    uuid = Column(String, unique=True)



