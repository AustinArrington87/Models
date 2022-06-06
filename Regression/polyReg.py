import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
import pandas as pd
import numpy

#x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
#y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

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
x = df['org_c']
y = df['stock_c']

# Model
# third degree polynomial (change last number to change degree)
polyModel = numpy.poly1d(numpy.polyfit(x, y, 3))

#Stats
print("R2: ", r2_score(y, polyModel(x)))
slope, intercept, r, p, std_err = stats.linregress(x,y)

# test model
# Predict future Values 
test_C = 2.14
test_C_stock = polyModel(test_C)
print("C Stock Prediction (T/acre): ", test_C_stock)

# Plotting
# specify how line will display - first to last position
#myLine = numpy.linspace(1, 22, 100)
#myLine = numpy.linspace(x[0], x[-1], 100)
myLine = numpy.linspace(1.5, 3.5, 100)
plt.scatter(x, y)
plt.plot(myLine, polyModel(myLine), color="red")
plt.xlabel("SOC %")
plt.ylabel("Stock SOC (tonnes/acre)")
plt.show()
