from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, HttpUrl
from enum import Enum
from datetime import datetime


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class PatientGetResponse(BaseModel):
    first_name:str
    middle_name:Optional[str]=None
    last_name:str
    age:int
    gender:Gender

class PatientGetRequest(BaseModel):
    first_name:str
    middle_name:Optional[str]=None
    last_name:str
    age:int
    gender:Gender
class PatientCreateRequest(BaseModel):
    first_name : str
    middle_name : Optional[str] = None
    last_name : str
    age : int
    gender : Gender


class RecordBase(BaseModel):
    radius_worst:float
    perimeter_worst:float
    area_worst:float
    perimeter_mean:float
    radius_mean:float
    area_mean:float
    concavity_worst:float
    concavity_mean:float
    concave_points_mean:float
    concave_points_worst:float
    created_at:datetime
    
class Record(RecordBase):
    id:UUID
    patient_id:UUID
    
    class Config:
        orm_node=True
       
class PatientBase(BaseModel):
    first_name:str
    middle_name:Optional[str]=None
    last_name:str
    age:int
    gender:Gender
    created_at:datetime
    
    
class Patient(PatientBase):
    id:UUID
    records: list[Record]=[]
    
    class Config:
        orm_node=True

    
class PatientUpdateRequest(BaseModel):
    first_name : Optional[str] = None
    middle_name : Optional[str] = None
    last_name : Optional[str] = None
    age : Optional[int] = None
    gender : Optional[Gender] = None
    

class RecordCreateRequest(BaseModel):
    patient_id: UUID
    radius_worst:float
    perimeter_worst:float
    area_worst:float
    perimeter_mean:float
    radius_mean:float
    area_mean:float
    concavity_worst:float
    concavity_mean:float
    concave_points_mean:float
    concave_points_worst:float
    prediction:str
    

class RecordCreateResponse(BaseModel):
    
    prediction:int

class RecordGetResponse(BaseModel):
    id:UUID
    firstname:str
    last_name:str
    age:int
    gender:Gender
    radius_worst:float
    perimeter_worst:float
    area_worst:float
    perimeter_mean:float
    radius_mean:float
    area_mean:float
    concavity_worst:float
    concavity_mean:float
    concave_points_mean:float
    concave_points_worst:float
    created_at : datetime
    prediction : str
    # patient:list[PatientGetRequest] =[]