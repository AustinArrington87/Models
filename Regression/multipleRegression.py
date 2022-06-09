import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
import statsmodels.api as sm

#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

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
X = df[['org_c', 'lat']]
y = df['stock_c']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedStockC = regr.predict([[16, 42.7]])
print("Predicted Stock C (t/acre C): ", predictedStockC[0])

# coefficients 
print("Coefficient: ", regr.coef_)

# Statistics 
X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())
