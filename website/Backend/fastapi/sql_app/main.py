import datetime, requests
from typing import List

from sqlalchemy.sql.sqltypes import JSON
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, query

from . import crud, models, schemas
from .database import SessionLocal, engine
origins = [
    "http://localhost",
    "http://127.0.0.1:3000/*",
    "*"
]



models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#------------ USERS --------------

@app.post("/users/")#, response_model=schemas.Membre) 
def create_user(user: schemas.Membre, db: Session = Depends(get_db)):
    #db_user = crud.get_user_by_email(db, email=user.email)
    db_user = False
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    items = crud.get_users(db)
    return items

@app.get("/users/{id}")
def get_user(db: Session = Depends(get_db), id= id):
    item = crud.get_user(db,id)
    return item

@app.delete("/users/{id}")
def delete_user(db: Session = Depends(get_db), id= id):
    return crud.delete_user(db,id)


#------------ PVS --------------

@app.post("/pvs/") 
def create_pv(pv: schemas.Pv, db: Session = Depends(get_db)):
    return crud.create_pv(db=db, pv=pv)

@app.get("/pvs/")
def get_pvs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_pvs(db, skip=skip, limit=limit)
    return items

@app.get("/pvs/{id}")
def get_pv(db: Session = Depends(get_db), id= id):
    item = crud.get_pv(db,id)
    return item

@app.delete("/pvs/{id}")
def delete_pv(db: Session = Depends(get_db), id= id):
    return crud.delete_pv(db,id)

#--------- Auth -----------

data = {
'mock_data': 'true',
'ip_address': '92.188.61.181',
'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30'}
h  =  {'Content-Type': 'application/json'}
url = "http://endznai466euy82.m.pipedream.net"
response = requests.post(url, data,headers=h)
print(response)

#------------ REUNION --------------

@app.post("/reunion/") 
def create_reunion(obj: schemas.ReunionCreation, db: Session = Depends(get_db)):
    l=""
    if obj.o1:
        l+=str(obj.o1)+" "
    if obj.o2:
        l+=str(obj.o2)+" "
    if obj.o3:
        l+=str(obj.o3)+" "
    if obj.o4:
        l+=str(obj.o4)+" "
    print(obj)
    forword = schemas.Reunion(date =datetime.datetime.strptime(obj.date, "%Y-%m-%d"),
    conseil = obj.conseil , ordres = l)
    print(forword)
    return crud.create_reunion(db,forword)

@app.get("/reunion/")
def get_reunions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_reunions(db, skip=skip, limit=limit)
    return items

@app.get("/reunion/{id}")
def get_reunion(db: Session = Depends(get_db), id= id):
    item = crud.get_reunion(db,id)
    return item

@app.delete("/reunion/{id}")
def delete_reunion(db: Session = Depends(get_db), id= id):
    return crud.delete_reunion(db,id)

 #-----Ordre ------------
@app.post("/ordre")
def create_ordre(obj: schemas.Ordre, db: Session = Depends(get_db)):
    item = crud.create_ordre(db,obj)
    return item

@app.get("/ordre")
def get_ordres(db: Session = Depends(get_db)):
    items = crud.get_ordres(db)
    return items

@app.get("/ordre/{id}")
def get_ordre(db: Session = Depends(get_db), id = id):
    item = crud.get_ordre(db,id)
    return item 

#------------ PROPOSITIONS --------------

@app.post("/propo/") 
def create_proposition(obj: schemas.Proposition, db: Session = Depends(get_db)):
    return crud.create_proposition(db,obj)

@app.get("/propo/")
def get_props(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_props(db, skip=skip, limit=limit)
    return items

@app.get("/propo/{id}")
def get_prop(db: Session = Depends(get_db), id= id):
    item = crud.get_prop(db,id)
    return item

@app.delete("/propo/{id}")
def delete_prop(db: Session = Depends(get_db), id= id):
    return crud.delete_prop(db,id)

#------------ DOCTORANT --------------
@app.post("/doctorant/") 
def create_doctorant(obj: schemas.Doctorant, db: Session = Depends(get_db)):
    return crud.create_doctorant(db,obj)

@app.get("/doctorant/")
def get_doctorants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_doctorants(db, skip=skip, limit=limit)
    return items

@app.get("/doctorant/{id}")
def get_doctorant(db: Session = Depends(get_db), id= id):
    item = crud.get_doctorant(db,id)
    return item

@app.delete("/doctorant/{id}")
def delete_doctorant(db: Session = Depends(get_db), id= id):
    return crud.delete_doctorant(db,id)

#------------ DECRIT --------------

@app.post("/decrit/") 
def create_decrit(obj: schemas.Decrit, db: Session = Depends(get_db)):
    return crud.create_decrit(db,obj)

@app.get("/decrit/")
def get_decrit(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_decrits(db, skip=skip, limit=limit)
    return items

@app.get("/decrit/{id}")
def get_decrit(db: Session = Depends(get_db), id= id):
    item = crud.get_decrit(db,id)
    return item

@app.delete("/decrit/{id}")
def delete_decrit(db: Session = Depends(get_db), id= id):
    return crud.delete_decrit(db,id)

