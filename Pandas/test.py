import pandas as pd

mydataset = {
	'cars': ["BMW", "Volvo", "Ford"],
	'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print (myvar)

### SERIES ==> this is a column 
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])
# LABELS --> by default [0] is first index, but can create your own index 
a = [1, 7, 2]
myvar = pd.Series(a, index= ["x", "y", "z"])
print(myvar["x"])

# KEY/VALUE Objects as Series 
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar['day1'])

# DATA FRAME  - Series is column, Data Frame is whole table 
data = {
	"calories": [420, 380, 390],
	"duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

# DATA FRAME - Locate Row 
print(df.loc[[0, 1]])
# Add INDEX 

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day1"])

#### LOAD CSV into DataFrame 

df = pd.read_csv('snw-soc.csv')
print(df)
print(df['org_c'])
# hint - print entire DataFrame using to_string()
# print(df.to_string())
# you can change the max rows displayed 
# print(pd.options.display.max_rows)
# pd.options.display.max_rows = 9999

# shape of data? - 230 entries, 8 features/columns
print(df.shape)










