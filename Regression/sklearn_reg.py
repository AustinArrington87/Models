import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import AdaBoostRegressor

# https://towardsdatascience.com/simple-linear-regression-model-using-python-machine-learning-eab7924d18b4

#### LOAD CSV into DataFrame 

df = pd.read_csv('soc.csv')
print(df)
# shape of data? 
print(df.shape)
# display beginning of data
print(df.head())
# print column names 
for col in df.columns:
	print(col)

# Simple Linear Regression - Create X & Y
X = df['org_c']
y = df['stock_c']

# Create Training and Test datasets - 7:3 ratio 
# use train_test_split from sklearn.model_selection 
X_train_lm, X_test_lm, y_train_lm, y_test_lm = train_test_split(X, y, train_size = 0.7,
													test_size = 0.3, random_state = 100)

print(X_train_lm)
print(y_train_lm)

# need to add column to perform regression fit 
print(X_train_lm.shape)
# add additional column 
X_train_lm = X_train_lm.values.reshape(-1,1)
X_test_lm = X_test_lm.values.reshape(-1,1)
print(X_train_lm.shape)
print(X_test_lm.shape)

# Create Linear Regression Object 
lm = LinearRegression()
lm.fit(X_train_lm, y_train_lm)

# print coefficients 
intercept = lm.intercept_
print("Intercept: ", intercept)
# slope 
slope = lm.coef_
print('Slope: ', slope)

# y_pred = slope*X + intercept

# make predictions of y_value 
y_train_pred = lm.predict(X_train_lm)
y_test_pred = lm.predict(X_test_lm)
# comare the R2 of training and test data 
print(r2_score(y_train_lm,y_train_pred))
print(r2_score(y_test_lm,y_test_pred))

# compare simple linear with AdaBoost Regressor
# define the model
model = AdaBoostRegressor()
# fit the model on the whole dataset
model.fit(X_train_lm, y_train_lm)
# make predictions of y_value 
y_train_pred_ada = model.predict(X_train_lm)
y_test_pred_ada = model.predict(X_test_lm)
# compare R2 of training and test data
print(r2_score(y_train_lm, y_train_pred_ada))
print(r2_score(y_test_lm,y_test_pred_ada))
