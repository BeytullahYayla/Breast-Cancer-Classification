# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:09:04 2023

@author: Beytullah
"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split,GridSearchCV

class Knn_Classifier:
    def __init__(self,n_neighbors,X_train,y_train,X_test,y_test):
        self.n_neighbors=n_neighbors
        self.X_train=X_train
        self.y_train=y_train
        self.y_test=y_test
        self.X_test=X_test
        self.model=KNeighborsClassifier(n_neighbors=self.n_neighbors)
        self.model.fit(self.X_train, self.y_train)
        
    def get_model(self):
        return self.model
        
        
        
        
    def get_test_acc(self):
       
        
        
        
        y_pred=self.model.predict(self.X_test)
    
        test_accuracy=accuracy_score(self.y_test, y_pred)
        print(f"Accuracy is {test_accuracy}")
        
        return test_accuracy
    def get_train_acc(self):
        
       
        y_pred=self.model.predict(self.X_train)
    
        train_acc=accuracy_score(self.y_train, y_pred)
        print(f"Accuracy is {train_acc}")
        
        return train_acc
    
    def get_confusion_matrix(self):
        confusion_matris=confusion_matrix(self.y_test, self.y_pred)
        print(f"Confusion_matris is {confusion_matris}")
        
        return confusion_matris
    
    def get_scores_with_best_params(self):
        
        k_range=list(range(1,31))
        weight_options=["uniform","distance"]
        print()
        param_grid=dict(n_neighbors=k_range,weights=weight_options)
        
        grid=GridSearchCV(self.model,param_grid=param_grid)
        grid.fit(self.X_train, self.y_train)
        
        print(f"Best training score {grid.best_score_} with parameters : {grid.best_params_}")
        knn_model=KNeighborsClassifier(**grid.best_params_)
        knn_model.fit(self.X_train,self.y_train)
        
        #Train ve test scorelarını bul
        
        
        y_pred_test=knn_model.predict(self.X_test)
        y_pred_train=knn_model.predict(self.X_train)
        
        train_acc=accuracy_score(self.y_train, y_pred_train)
        test_acc=accuracy_score(self.y_test, y_pred_test)
        
        print(f"Train acc with best params :{train_acc} \n Test acc with best params {test_acc}")
        
        return train_acc,test_acc,knn_model
        
        
        
        