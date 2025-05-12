import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# load dataset
df = pd.read_excel("C:/Users/marck/OneDrive - OST/OST RJ/WING/WING - 4 Semester/MOSIM/Python Systemanalyse/Uebung 4_2_1.xlsx")
print(df.head())
print(df.tail())

# use only one feature
x = df[["t in sec"]].values
y = df[["dist in m"]].values
z = df[["y_squared"]].values

# split data into training/testing sets
range   = 10 #must be symmetric
x_train = x[:-range]
x_test  = x[-range:]
y_train = y[:-range]
y_test  = y[-range:]

# generate y^2 in a new coloumn which is bsclly t^2
# df["y_squared"] = df.series([1, 3, 5, np.nan, 6, 8])
# df['y_squared'] = df.apply(lambda y: y_squared(row), axis=1)

# y_squared = pow(y, y)
# df = pd.DataFrame({"y_squared" : [10,20]})
# df["y_squared"] = df.apply(bla row: row.Cost - )

# create linear regression object and train model
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)

# make predictions using the testing set
y_pred = regr.predict(x_test)

# the coefficients and mean squared error
print("Coefficients: \n", regr.coef_)
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

# plot outputs
plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, y_pred, color="blue", linewidth=3)

# plot label and grid axis
plt.xlabel("time in s")
plt.ylabel("distance in m")
plt.title("Acceleration evaluation")
plt.grid()

plt.show()