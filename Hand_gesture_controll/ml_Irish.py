from statistics import mode
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from sklearn.metrics import mean_squared_error
from sklearn import linear_model, preprocessing
import pandas as pd
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

# x=(np.random.normal(50,100,100)).astype(int)
# y=(np.random.normal(25,50,100)).astype(int)

df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                names=["Sepal Length","Sepal Width","Petal Length","Petal Width","Class"])
print(df)
model=linear_model.LinearRegression()

feature_data=df[["Sepal Length","Sepal Width","Petal Length","Petal Width"]]
labels_data=df["Class"]
train_labels=[]
for i in range(0,np.size(labels_data)):
    if labels_data[i]=="Iris-setosa":
        train_labels.append(1)
    elif labels_data[i]=="Iris-versicolor":
        train_labels.append(2)
    elif labels_data[i]=="Iris-virginica":
        train_labels.append(3)

train_x=feature_data[5:145]
train_y=train_labels[5:145]
model.fit(train_x,train_y)

test_x=(feature_data[80:110])
print(train_labels[80:110])
print(model.predict(test_x))