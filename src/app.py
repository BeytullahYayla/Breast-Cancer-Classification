from fastapi import FastAPI,Query,Path
from pydantic import BaseModel
import numpy as np
import pickle
import uvicorn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.neighbors import KNeighborsClassifier
# from  sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import NeighborhoodComponentsAnalysis,LocalOutlierFactor
import pickle
from input_data import input_data
from fastapi.middleware.cors import CORSMiddleware



"""start app"""
app=FastAPI(title="Cancer Prediction App")

origins = [
    
    "http://localhost:4200"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""acquire and transform  data"""
data_df=pd.read_csv("../data.csv")
data_df.drop(["Unnamed: 32",'id'],inplace=True,axis=1)

data_df=data_df.rename(columns={"diagnosis":"target","concave points_worst":"concave_points_worst","concave points_mean":"concave_points_mean",
                                "concave points_se":"concave_points_se"
                                
                                })
data_df["target"]=[1 if i.strip()=="M" else 0 for i in data_df.target]

X=data_df.drop(["target"],axis=1)
y=data_df["target"]

cols=X.columns.tolist()

"""train-test-splitting for accuracy evaluation"""

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)


"""Model that we saved earlier"""
model=pickle.load(open("knn.sav","rb"))




@app.get("/")
def home():
    return "Api is working as expected"

@app.post("/predict")
def predict_without_nca(data:input_data):
  
 
    data=pd.DataFrame(data.to_dict(),columns=X.columns.tolist(),index=[0])
   
    print(data)

    
    prediction=model.predict(data)
    return {"prediction":prediction.tolist()}

@app.get("/getevaluationScores")
def getEvaluationScores():
    predictions_test=model.predict(X_test)
    predictions_train=model.predict(X_train)
    test_acc=accuracy_score(predictions_test,y_test)
    train_acc=accuracy_score(predictions_train,y_train)
    return {"test_accuracy":test_acc,"train_acc":train_acc}

        
if __name__=="__main__":
     uvicorn.run(app,host="127.0.0.1",port=8000)