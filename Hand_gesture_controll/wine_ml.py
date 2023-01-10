from cProfile import label
from operator import index
from pyexpat import model
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()

df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv")

df=df['fixed acidity;"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality"'].str.split(';',expand=True)

df.rename({0:'fixed acidity',1:"volatile acidity",2:'citric acid',3:"residual sugar",4:"chlorides",5:"free sulfur",6:'total sulfur',
            7:"density",8:"pH",9:"sulphates",10:"alcohol",11:"quality"},axis=1,inplace=True)

print(np.min(df['quality']),np.max(df['quality']))

feature_data=df[['fixed acidity',"volatile acidity",'citric acid',"residual sugar","chlorides","free sulfur",'total sulfur',"density","pH","sulphates","quality"]]
label_data=df['alcohol']

train_X=feature_data[100:4000]
train_y=label_data[100:4000]

model=linear_model.LinearRegression()

model.fit(train_X,train_y)
print(mean_squared_error(train_y,model.predict(train_X)))
print(label_data[20:50]);
print(model.predict(feature_data[20:50]))