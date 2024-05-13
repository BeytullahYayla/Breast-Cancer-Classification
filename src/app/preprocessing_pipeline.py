from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator,TransformerMixin
import pandas as pd
import numpy as np

class ColumnDropper(BaseEstimator,TransformerMixin):
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        return X.drop(["Unnamed: 32",'id'],axis=1)

class ColumnRenamer(BaseEstimator,TransformerMixin):
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        return X.rename(columns={"diagnosis":"target","concave points_worst":"concave_points_worst",
                                 "concave points_mean":"concave_points_mean",
                                "concave points_se":"concave_points_se"
                                })
class CategoricalDataEncoder(BaseEstimator,TransformerMixin):
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        X["target"]=[1 if i.strip()=="M" else 0 for i in X.target]
        return X

class TargetColumnDropper(BaseEstimator,TransformerMixin):
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        
        return  X.drop(["target"],axis=1)

    









