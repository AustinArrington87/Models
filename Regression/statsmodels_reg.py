import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import r2_score

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

#sns.pairplot(df, x_vars=['org_c', 'lat', 'lon'], y_vars='stock_c', height=4, aspect=1, kind='scatter')
#plt.show()

# Simple Linear Regression - Create X & Y
X = df['org_c']
y = df['stock_c']

# Create Training and Test datasets - 7:3 ratio 
# use train_test_split from sklearn.model_selection 
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7,
													test_size = 0.3, random_state = 100)

print(X_train)
print(y_train)


# Linear Regression y = mX + b 
# add constant to get intersect 
X_train_sm = sm.add_constant(X_train)
# fit regression with OLS (Ordinary Least Square)
lr = sm.OLS(y_train, X_train_sm).fit()
# paramaters 
print(lr.params)
# summary statistics 
print(lr.summary())
# Create Lin Regression Model
constant = lr.params[0]
coefficient = lr.params[1]
print("Constant: ", constant)
print("Coefficient: ", coefficient)

# scatter plot 
plt.scatter(X_train,y_train)
plt.plot(X_train, constant + coefficient*X_train, 'r')
plt.xlabel("SOC %")
plt.ylabel("Stock SOC (tonnes/acre")
plt.show()


# now predict y value from training dataset of X using 'oreduxct attribute'
# after this create error terms (Residuals) from predicted data 

# predicting y_value using X taining data
y_train_pred = lr.predict(X_train_sm)
# create residuals from y_train data and predicted y_data
res = (y_train - y_train_pred)
# plotting histogram using residual values 
fig = plt.figure()
sns.distplot(res, bins = 15)
plt.title('Error Terms', fontsize = 15)
plt.xlabel('y_train - y_train_pred', fontsize = 15)
plt.show()
# residuals should follow normal distribution graph with mean 0 
# check if residuals are following any specific pattern 
plt.scatter(X_train,res)
plt.show()

# PREDICTIONS on test value AKA Model Evaluation 
# fit the model with the Test dataset (just like we did w Training above)
X_test_sm = sm.add_constant(X_test)
y_test_pred = lr.predict(X_test_sm)
print("SOC Stock Predictions")
print(y_test_pred)
# calculate R2 for above-predicted y values 
r_squared = r2_score(y_test, y_test_pred)
print("Linear Reg Model R2: ", r_squared)
# R2 on test = 0.166
# compare back to R2 on training data (0.114)
# if R2 on test data within 5% of R2 training data, model is stable 
plt.scatter(X_test, y_test)
plt.plot(X_test, y_test_pred, 'r')
plt.title('SOC Stock Model Prediction')
plt.xlabel('SOC %')
plt.ylabel('Stock SOC (tonnes/acre')
plt.show()


