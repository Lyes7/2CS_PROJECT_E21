from datetime import date
import uuid
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import Integer, String
import shortuuid

from . import models, schemas


#def get_user(db: Session, user_id: int):
#    return db.query(models.User).filter(models.User.id == user_id).first()


#def get_user_by_email(db: Session, email: str):
#    return db.query(models.User).filter(models.User.email == email).first()


#def get_users(db: Session, skip: int = 0, limit: int = 100):
#    return db.query(models.User).offset(skip).limit(limit).all()



def create_user(db: Session, user: schemas.Membre):
    fake_hashed_password = user.hashed_password + "notreallyhashed"
    uid = 'a'+ str(uuid.uuid4())[1:-1]
    db_user = models.Membre(
        email=user.email, 
        hashed_password=fake_hashed_password, 
        tel=user.tel,
        userID= user.userID,
        uuid= uid,
        is_president=user.is_president,
        signature=user.signature)       
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Membre).offset(skip).limit(limit).all()

def get_user(db: Session, id: Integer):
    return db.query(models.Membre).filter_by(id=id).first()

def delete_user(db: Session, id: Integer):
    item = get_user(db,id)
    db.delete(item)
    db.commit()
    return item

def create_pv(db: Session, pv: schemas.Pv):
    uid = 'a'+ str(uuid.uuid4())[1:-1]
    db_pv = models.Pv(
        membres = pv.membresPresent,
        date = pv.date,
        uuid = uid,
        ordres = pv.ordres
       )
    db.add(db_pv)
    db.commit()
    db.refresh(db_pv)
    return db_pv

def get_pvs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pv).offset(skip).limit(limit).all()

def get_pv(db: Session, id: Integer):
    return db.query(models.Pv).filter_by(id=id).first()

def delete_pv(db: Session, id: Integer):
    item = get_pv(db,id)
    db.delete(item)
    db.commit()
    return item


def create_ordre(db: Session, rn: schemas.Ordre):
    uid = 'a'+ str(uuid.uuid4())[1:-1]
    db_rn = models.ordre(
    abv = rn.abv,
    titre = rn.titre,
    validation = rn.validation,
    motif = rn.motif,
    uuid = uid 
    )
    db.add(db_rn)
    db.commit()
    db.refresh(db_rn)
    return db_rn

def get_ordres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ordre).offset(skip).limit(limit).all()


def get_ordre(db: Session, abv: String):
    return db.query(models.ordre).filter_by(abv=abv).first()





def create_reunion(db: Session, rn: schemas.Reunion):
    uid = 'a'+ str(uuid.uuid4())[1:-1]
    db_rn = models.Reunion(
    date = rn.date,
    conseil = rn.conseil,
    ordres = rn.ordres,
    uuid = uid 
    )
    db.add(db_rn)
    db.commit()
    db.refresh(db_rn)
    return db_rn

def get_reunions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reunion).offset(skip).limit(limit).all()

def get_reunion(db: Session, id: Integer):
    return db.query(models.Reunion).filter_by(id=id).first()

def delete_reunion(db: Session, id: Integer):
    item = get_reunion(db,id)
    db.delete(item)
    db.commit()
    return item

def create_proposition(db: Session, obj: schemas.Proposition):
    uid = 'a'+ str(uuid.uuid4())[1:-1]
    db_obj = models.Proposition(
    titre = obj.titre,
    validation = obj.validation,
    uuid = uid)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_props(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Proposition).all()

def get_prop(db: Session, id: Integer):
    return db.query(models.Proposition).filter_by(id=id).first()

def delete_prop(db: Session, id: Integer):
    item = get_prop(db,id)
    db.delete(item)
    db.commit()
    return item

def create_doctorant(db: Session, obj: schemas.Doctorant):
    uid = 'a'+ str(uuid.uuid4())[1:-1]
    db_obj = models.Doctorant(
        nom = obj.nom,
        prenom = obj.prenom,
        propositions = obj.propositions,
        uuid = uid
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_doctorants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctorant).offset(skip).limit(limit).all()

def get_doctorant(db: Session, id: Integer):
    return db.query(models.Doctorant).filter_by(id=id).first()

def delete_doctorant(db: Session, id: Integer):
    item = get_doctorant(db,id)
    db.delete(item)
    db.commit()
    return item

def create_decrit(db: Session, obj: schemas.Decrit):
    uid = 'a'+ str(uuid.uuid4())[1:-1]
    db_obj = models.Decrit(
        numero = obj.numero,
        description = obj.description,
        date = obj.date,
        uuid = uid
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_decrits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Decrit).offset(skip).limit(limit).all()

def get_decrit(db: Session, id: Integer):
    return db.query(models.Decrit).filter_by(id=id).first()

def delete_decrit(db: Session, id: Integer):
    item = get_decrit(db,id)
    db.delete(item)
    db.commit()
    return item
