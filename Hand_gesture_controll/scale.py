import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
scale=StandardScaler()

df=pd.read_csv("/home/azad/Downloads/cars.csv")
data=df[["Weight","Volume"]]
y=df["CO2"]
resize_data=scale.fit_transform(data)
# print(resize_data)

regrr=linear_model.LinearRegression()
regrr.fit(data,y)
print(regrr.coef_)

scaled = scale.transform([[2300, 1.3]])
print(regrr.predict([scaled[0]]))
print(regrr.intercept_)