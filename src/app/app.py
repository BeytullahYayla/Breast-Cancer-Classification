from fastapi import FastAPI,Query,Path
from pydantic import BaseModel
import numpy as np
import pickle
import uvicorn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import NeighborhoodComponentsAnalysis,LocalOutlierFactor
import pickle
from input_data import input_data
from fastapi.middleware.cors import CORSMiddleware
from preprocessing_pipeline import ColumnDropper,TargetColumnDropper,ColumnRenamer,CategoricalDataEncoder
from sklearn.pipeline import Pipeline
from connect_database import engine, SessionLocal
from fastapi import FastAPI, HTTPException, Depends, status, Query, UploadFile, File, encoders
from pydantic import BaseModel
from typing import Annotated, Optional
import tables
from models import Patient,Record,PatientCreateRequest,PatientGetResponse,PatientUpdateRequest,RecordCreateRequest,RecordCreateResponse,RecordGetResponse
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from sqlalchemy import create_engine, Column, String, select, desc
import numpy as np
from PIL import Image
from typing import Annotated
from passlib.context import CryptContext
from passlib.hash import bcrypt
import secrets
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import func
from typing import List


"""start app"""

app=FastAPI(title="Cancer Prediction App")

origins = [
    
    "http://localhost:4200",
    "http://localhost:8000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tables.Base.metadata.create_all(bind=engine)


pipe_X=Pipeline([
    ("column_dropper",ColumnDropper()),
    ("column_renamer",ColumnRenamer()),
    ("categorical_data_encoder",CategoricalDataEncoder()),
    ("target_data_dropper",TargetColumnDropper())
])
pipe_y=Pipeline([
    ("column_dropper",ColumnDropper()),
    ("column_renamer",ColumnRenamer()),
    ("categorical_data_encoder",CategoricalDataEncoder()),
])


"""acquire and transform  data"""
data_df=pd.read_csv("data.csv")
print(data_df)
new_cols_X=["radius_worst","perimeter_worst","area_worst","perimeter_mean","radius_mean","area_mean","concavity_worst","concavity_mean","concave_points_mean","concave_points_worst"]
X=pipe_X.fit_transform(data_df)
X=X[new_cols_X]
print(X)

y=pipe_y.fit_transform(data_df)["target"]


cols=X.columns.tolist()

"""train-test-splitting for accuracy evaluation"""

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)


"""Model that we saved earlier"""
model=pickle.load(open("knn.sav","rb"))
print(model)


def get_database_connection():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

db_dependency = Annotated[Session, Depends(get_database_connection)]
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_patient(patient:PatientCreateRequest,db:db_dependency):

    db_user = tables.Patient(**patient.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
    
def get_patient(db: db_dependency, firstname: str):
    return db.query(tables.Patient).filter(tables.Patient.first_name == firstname).first()
def get_patient_by_id(db: db_dependency, id: int):
    return db.query(tables.Patient).filter(tables.Patient.id == id).first()

async def get_pateint_by_firstname(firstname:str, db:db_dependency):

    query = select(tables.Patient).where(tables.Patient.first_name == firstname)
    user = db.execute(query).scalars().all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return user[0].id

async def create_patient(patient:PatientCreateRequest, db:db_dependency):
    print(patient)
    db_patient = tables.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def predict(data:pd.DataFrame):
    prediction=model.predict(data)
    return prediction.tolist()

def delete_patient_by_id(db: Session, patient_id: str):
    patient = db.query(tables.Patient).filter(tables.Patient.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
        return True  # Başarıyla silindi
    return False  # Hasta bulunamadı
async def update_existing_patient(patient_id: int, patient_update: PatientUpdateRequest, db: db_dependency):
    # Veritabanında mevcut hastayı güncelle
    
    # Veritabanından hasta bilgilerini al
    patient = get_patient_by_id(db, patient_id)
    
    if not patient:
        raise HTTPException(status_code=404, detail="Hasta bulunamadı.")
    
    # Güncellenecek alanları güncelle
    patient.first_name = patient_update.first_name
    patient.middle_name = patient_update.middle_name
    patient.last_name = patient_update.last_name
    patient.age = patient_update.age
    patient.gender = patient_update.gender
    
    # Veritabanına güncellenmiş hasta bilgilerini kaydet
    db.commit()
    db.refresh(patient)
    
    return patient
def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(tables.Patient).offset(skip).limit(limit).all()
@app.get("/")
def home():
    return "Api is working as expected"

@app.post("/predict")
def predict_without_nca(data:input_data):
  
    data=pd.DataFrame(data.to_dict(),columns=X.columns.tolist(),index=[0])

    return {"prediction":predict(data)}


@app.post("/addPatient",status_code=status.HTTP_200_OK)
async def add_patient(db: db_dependency, patient:PatientCreateRequest):
    patientx=get_patient(db,patient.first_name)
    if patientx:
        raise HTTPException(status_code=400, detail="Lütfen başka bir kullanıcı adı girin.")
    
    return await create_patient(patient,db)
@app.post("/updatePatient", status_code=status.HTTP_200_OK)
async def update_patient(db: db_dependency, patient_update: PatientUpdateRequest):
    # İlgili hasta adıyla mevcut hastayı bul
    patientx = get_patient(db, patient_update.first_name)
    
    if not patientx:
        raise HTTPException(status_code=404, detail="Hasta bulunamadı.")
    
    # Hasta bilgilerini güncelle
    updated_patient = await update_existing_patient(patientx.id, patient_update, db)
    
    return updated_patient



@app.delete("/patients/{patient_id}", status_code=204)
def delete_patient(patient_id: str,db:db_dependency):
    success = delete_patient_by_id(db, patient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Hasta bulunamadı")
    return {"detail": "Hasta başarıyla silindi"}

@app.get("/patients/",response_model=List[Patient])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_database_connection)):
    patients = get_patients(db, skip=skip, limit=limit)
    return patients

@app.post("/savePrediction", status_code=status.HTTP_200_OK)
async def save_prediction(db: db_dependency, patient_name: str, data: input_data):
    data = pd.DataFrame(data.to_dict(), columns=X.columns.tolist(), index=[0])
    prediction = predict(data)
    
    if prediction[0] == 0:
        pred = "Malignant"
    else:
        pred = "Benign"
        
    if not prediction:
        raise HTTPException(status_code=400, detail="Bir hatadan dolayı tahmin yapılamadı")
   
    patient_id = await get_pateint_by_firstname(patient_name, db)  # Hasta ID'sini alın
    
    # Hasta ID'sini doğru şekilde UUID nesnesine dönüştürün
    patient_uuid = UUID(patient_id)
    
    # Hexadecimal string temsilini alın
    patient_hex = patient_uuid.hex
    
    # RecordCreateRequest nesnesini oluşturun
    record_data = {
        "patient_id": patient_hex,
        "radius_worst": data.radius_worst,
        "perimeter_worst": data.perimeter_worst,
        "area_worst": data.area_worst,
        "perimeter_mean": data.perimeter_mean,
        "radius_mean": data.radius_mean,
        "area_mean": data.area_mean,
        "concavity_worst": data.concavity_worst,
        "concavity_mean": data.concavity_mean,
        "concave_points_mean": data.concave_points_mean,
        "concave_points_worst": data.concave_points_worst,
        "prediction": pred
    }
    
    # RecordCreateRequest nesnesini kullanarak Record oluşturun
    new_record = RecordCreateRequest(**record_data)
    
    # Veritabanına kaydedin
    db_records = tables.Record(**new_record.model_dump())
    db.add(db_records)
    db.commit()
    db.refresh(db_records)
    
    return prediction

  
    
    
    
        
if __name__=="__main__":
     
     uvicorn.run(app,host="127.0.0.1",port=8000)
