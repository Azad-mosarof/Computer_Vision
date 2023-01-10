import numpy as np
import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

df=pd.read_csv("/home/azad/Downloads/cars.csv")
# print(df)
X=df[["Weight","Volume"]]
y=df["CO2"]

regrr=linear_model.LinearRegression()
regrr.fit(X,y)
print(regrr.predict([[2300,1300]]))
print(regrr.coef_)
print(r2_score(y,regrr.predict(X)))



