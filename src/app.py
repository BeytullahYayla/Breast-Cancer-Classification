from fastapi import FastAPI,Query,Path
from pydantic import BaseModel
import numpy as np
import pickle
import uvicorn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from  sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import NeighborhoodComponentsAnalysis,LocalOutlierFactor
import pickle
from input_data import input_data
import json

"""start app"""
app=FastAPI(title="Cancer Prediction App")

"""acquire data"""
data_df=pd.read_csv("../data.csv")
data_df.drop(["Unnamed: 32",'id'],inplace=True,axis=1)

data_df=data_df.rename(columns={"diagnosis":"target","concave points_worst":"concave_points_worst","concave points_mean":"concave_points_mean",
                                "concave points_se":"concave_points_se"
                                
                                })
data_df["target"]=[1 if i.strip()=="M" else 0 for i in data_df.target]

X=data_df.drop(["target"],axis=1)
y=data_df["target"]

cols=X.columns.tolist()





# def preprocess_data(data):
    
    
#     return X_reduced_nca



@app.get("/")
def home():
    return "Api is working as expected"

@app.post("/predict")
def predict(data:input_data):
  
    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)
    # nca=NeighborhoodComponentsAnalysis(n_components=2)
    # nca.fit(X_scaled,y)
    # print(data.to_dict())
    # model=pickle.load(open("best.sav","rb"))
    data=pd.DataFrame(data.to_dict(),columns=X.columns.tolist(),index=[0])
   
    print(data)
    # print(data.shape)
    # print("Error is here")
    # X_reduced_nca=nca.transform(data)
    # print(X_reduced_nca.shape)
    model=pickle.load(open("knn.sav","rb"))
    prediction=model.predict(data)
    return {"prediction":prediction}
        
if __name__=="__main__":
     uvicorn.run(app,host="127.0.0.1",port=8000)