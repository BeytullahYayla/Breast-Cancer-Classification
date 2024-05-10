from sqlalchemy import Boolean, Double, Column, DateTime, ForeignKey, Float, Integer, String, UUID, CHAR, Table, LargeBinary, BLOB
from connect_database import Base
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import relationship


class Patient(Base):
    
    __tablename__ = "patients"

    id = Column(CHAR(36), primary_key=True, index=True, default=uuid4, unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    age=Column(Integer(),nullable=False)
    gender = Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    records=relationship("Record",back_populates="patients",cascade="all, delete")
    
class Record(Base):
    
    __tablename__ = "records"
    
    id = Column(CHAR(36), primary_key=True, default=uuid4, unique=True, index=True)
    patient_id = Column(CHAR(36), ForeignKey('patients.id'))
    radius_worst = Column(Double(), nullable=True)
    perimeter_worst = Column(Double(), nullable=False)
    area_worst = Column(Double(),  nullable=False)
    perimeter_mean = Column(Double(), nullable=False)
    radius_mean = Column(Double(),nullable=False)
    area_mean = Column(Double(),nullable=False)
    concavity_worst=Column(Double(),nullable=False)
    concavity_mean=Column(Double(),nullable=False)
    concave_points_mean=Column(Double(),nullable=False)
    concave_points_worst=Column(Double(),nullable=False)
    prediction=Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    
    patients=relationship("Patient",back_populates="records")
    
