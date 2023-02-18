# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:14:42 2023

@author: Beytullah
"""
from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class visualization_helper():
    def __init__(self,model,y):
        self.cmap_light=ListedColormap(['orange','cornflowerblue'])
        self.cmap_bold=ListedColormap(['darkorange','darkblue'])
        self.model=model
        self.y=y
    
    
    def visualize_pca(self,pca_data,step_size):
        x_min,x_max=pca_data[:,0].min()-1,pca_data[:,0].max()+1
        y_min,y_max=pca_data[:,1].min()-1,pca_data[:,1].max()+1
        
        xx,yy=np.meshgrid(np.arange(x_min,x_max,step_size),np.arange(y_min,y_max,step_size))
        
        prediction=self.model.predict(np.c_[xx.ravel(),yy.ravel()])
        
        prediction.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx,yy,prediction,cmap=self.cmap_light)
        
        plt.scatter(pca_data[:,0],pca_data[:,1],c=y,cmap=self.cmap_bold,edgecolor="k",s=20)
        
        plt.xlim(xx.min(),xx.max())
        plt.ylim(yy.min(),yy.max())
        
        
        
        
    
    