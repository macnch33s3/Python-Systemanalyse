import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

#load dataset
df = pd.read_excel("C:/Users/marck/OneDrive - OST/OST RJ/WING/WING - 4 Semester/MOSIM/Python Systemanalyse/Uebung 4_2_1.xlsx")
print(df.head())
print(df.tail())

#use only one feature
x = df[["t in sec"]].values
y = df[["dist in m"]].values

#split data into training/testing sets
x_train = x[:-10]
x_test  = x[-10:]
y_train = y[:-10]
y_test  = y[-10:]

#create linear regression object and train model
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)

#make predictions using the testing set
y_pred = regr.predict(x_test)

#the coefficients
print("Coefficients: \n", regr.coef_)
#the mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
#the coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

#plot outputs
plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, y_pred, color="blue", linewidth=3)

#plot label and grid
plt.xlabel("time in s")
plt.ylabel("distance in m")
plt.title("Acceleration evaluation")
plt.grid()

plt.show()