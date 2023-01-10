# common use functions and method in pandas:
# Once Pandas is installed, import it in your applications by adding the import keyword:
# The version string is stored under __version__ attribute.(pd.__version__)
# series in pandas => myvar = pd.Series(a)
# With the index argument, you can name your own labels.ex=> myvar = pd.Series(a, index = ["x", "y", "z"])
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.ex=> df = pd.DataFrame(data)
# Pandas use the loc attribute to return one or more specified row(s). ex=> df.loc[[0, 1]]









import pandas as pd

# mydata={
#     'car':["BMW","Volvo","Hunda","Glamer","Tesla"],
#     'passings':[3,7,4,5,8],
#     'weight':[1000,3444,2444,888,3333]
# }
# print(pd.DataFrame(mydata))
# myvar=pd.Series(mydata['car'], index=('a','b','c','d','e'))
# print(myvar)
# print(myvar['c'])

# mydata={'day1':100,'day2':200,'day3':300,'day4':400}
# myvar=pd.Series(mydata)
# print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
mydata=pd.DataFrame(data,index=['day1','day2','day3'])
print(mydata.loc[['day2','day1']])
