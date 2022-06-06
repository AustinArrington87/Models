import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

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
x = df['org_c']
y = df['stock_c']

slope, intercept, r, p, std_err = stats.linregress(x,y)

def LinReg(x):
	return slope * x + intercept

# Linear Regression Model
LinearModel = list(map(LinReg, x))

# Print Stats
#R2 is explanatory value, closer r is to zero, weaker the linear relationship
print("R2: ", r)
# p value describes whether their is significant relationship described by the model
# Explantory power to be significatn (p < 0.05)
print("p: ", p)
print("Standard Error: ", std_err)
# The standard error(SE) is very similar to standard deviation. Both are measures of spread. The higher the number, the more spread out your data is. To put it simply, the two terms are essentially equal—but there is one important difference. While the standard error uses statistics (sample data) standard deviations use parameters (population data).
# Predict future Values 
test_C = 2.14
test_C_stock = LinReg(test_C)
print("C Stock Prediction (T/acre): ", test_C_stock)

# Scatterplot 

plt.scatter(x, y)
plt.plot(x, LinearModel, color="red")
plt.xlabel("SOC %")
plt.ylabel("Stock SOC (tonnes/acre)")
plt.show()
