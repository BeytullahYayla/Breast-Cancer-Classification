#%% Importing Required Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from  sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import NeighborhoodComponentsAnalysis,LocalOutlierFactor
from sklearn.decomposition import PCA
from knn_Classifier import Knn_Classifier
from visualization_helper import visualization_helper
import pickle

#warnings
import warnings
warnings.filterwarnings("ignore")

data_df=pd.read_csv("../data.csv")
data_df.drop(["Unnamed: 32",'id'],inplace=True,axis=1)

data_df=data_df.rename(columns={"diagnosis":"target"})

sns.countplot(data_df["target"])

print(data_df.target.value_counts())

data_df["target"]=[1 if i.strip()=="M" else 0 for i in data_df.target]

print(len(data_df))
print(f"Data shape: {data_df.shape}")

data_df.info()

description=data_df.describe()

"""

The mean values  between columns have too much difference. For example area_mean is 654.889 and radius_mean is 14.1273
*We can standardize our values so we can reduce computational cost.
*Big values can lead to biases.
*There is no missing values in our dataset
"""


# %% Explotary Data Analysis

#Correlation Matrix

corr_matrix=data_df.corr()
sns.clustermap(corr_matrix, annot=True,fmt=".2f")

plt.title("Correlation Between Features")
plt.show()



threshold=0.50
filter=np.abs(corr_matrix["target"])>threshold
corr_features=corr_matrix.columns[filter].tolist()

sns.clustermap(data_df[corr_features].corr(), annot=True, fmt=".2f")
plt.title("Correlation matrix with 0.75 threshold value")
plt.show()


##Box Plot

data_melted=pd.melt(data_df,id_vars="target",var_name="features",value_name="value")
sns.boxplot(x="features", y="value",hue="target",data=data_melted)

plt.xticks(rotation=90)
plt.show()

"""
sns.pairplot(data_df[corr_features],diag_kind="kde",markers="+",hue="target")
plt.show()
"""


##Outlier:Veri setimizde bulunan aykırı değerlerdir


# %% Outlier Detection

y=data_df["target"]
X=data_df.drop(["target"],axis=1)
columns=data_df.columns.tolist()

clf=LocalOutlierFactor()#Finds outliers

#LOF>1:Outlier
#LOF<1:Inlier

y_pred=clf.fit_predict(X)

#In y_pred matris if value equals to 1 inlier else outlier

X_score=clf.negative_outlier_factor_

outlier_score=pd.DataFrame()
outlier_score["score"]=X_score

threshold=-2.5
filter=outlier_score["score"]<threshold

radius=(X_score.max()-X_score)/(X_score.max()-X_score.min())
outlier_score["radius"]=radius


plt.figure()
plt.scatter(X.iloc[:,0],X.iloc[:,1],s=3,marker=("+"))



plt.scatter(X.iloc[:,0],X.iloc[:,1],s=1000*radius,edgecolors="r",facecolors="none",label="Outlier scores")
plt.show()

#%%Train-test-splitting

test_size=0.3
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=test_size,random_state=42)



X_train_description=X_train.describe()
X_train_description_df=pd.DataFrame(X_train_description)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

columns.pop(0)
##X_train ayır ve boxplot ile göster...
X_train_df=pd.DataFrame(X_train_scaled,columns=columns)
X_train_df_describe=X_train_df.describe()

X_train_df["target"]=y_train


data_melted=pd.melt(X_train_df,id_vars="target",var_name="features",value_name="value")

plt.figure()
sns.boxplot(x="features",y="value",data=data_melted,hue="target")
plt.xticks(rotation=90)
plt.show()

#%% KNN Algorithm
#Sensitive to outliers
#Easy to implement 
#Fast
#Curse of dimensionality
#Need to feature scaling

knn=Knn_Classifier(n_neighbors=2, X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
train_acc,test_acc=knn.get_scores_with_best_params()







#%% Principal Component Analysis

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

pca=PCA(n_components=2)
pca.fit(X_scaled)

X_reduced_pca=pca.transform(X_scaled)
pca_data=pd.DataFrame(X_reduced_pca,columns=["p1","p2"])
pca_data["target"]=y

sns.scatterplot(x="p1",y="p2",hue="target",data=pca_data)
plt.title("PCA: P1 vs P2")

X_train_pca,X_test_pca,y_train_pca,y_test_pca=train_test_split(X_reduced_pca,y,test_size=0.3,random_state=42)

model=KNeighborsClassifier(n_neighbors=2)
model.fit(X_train_pca, y_train_pca)
vh=visualization_helper(model=model, y=y)
vh.visualize_pca(X_reduced_pca, 0.05)

preds_test=model.predict(X_test_pca)
print(accuracy_score(y_test_pca, preds_test))#0.95 test accuracy score

preds_train=model.predict(X_train_pca)
print(accuracy_score(y_train_pca, preds_train))#0.94 test accuracy score


#%%Neighborhood Component Analysis

nca=NeighborhoodComponentsAnalysis(n_components=2)
nca.fit(X_scaled, y)
X_reduced_nca=nca.transform(X_scaled)
nca_data=pd.DataFrame(X_reduced_nca,columns=["p1","p2"])
nca_data["target"]=y

sns.scatterplot(x="p1",y="p2",hue="target", data=nca_data)
plt.title("NCA: P1 vs P2")

X_train_nca,X_test_nca,y_train_nca,y_test_nca=train_test_split(X_reduced_nca,y,test_size=0.3,random_state=42)

model=KNeighborsClassifier(n_neighbors=2)
model.fit(X_train_nca, y_train_nca)
vh=visualization_helper(model=model, y=y)
vh.visualize_pca(X_reduced_nca, 0.2)

preds_test=model.predict(X_test_nca)
print(accuracy_score(y_test_nca, preds_test))#0.98 test accuracy score

preds_train=model.predict(X_train_nca)
print(accuracy_score(y_train_nca, preds_train))#0.98 test accuracy score


#%%Save Best Model

pickle.dump(model, open("best.sav",'wb'))
