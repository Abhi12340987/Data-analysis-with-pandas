import os

print(os.listdir())

import pandas


df1 = pandas.read_csv("Data analysis with pandas\supermarkets.csv") #loading csv file using pandas and python
print(df1)

df2 = pandas.read_json("Data analysis with pandas\supermarkets.json") #loading json file using pandas and python
print(df2)

df3 = pandas.read_excel("Data analysis with pandas\supermarkets.xlsx", sheet_name=0) #loading an excel (xlsx) file
print(df3)

df4 = pandas.read_csv("Data analysis with pandas\supermarkets-commas.txt") #loading text based files with commas
print(df4)

df5 = pandas.read_csv("Data analysis with pandas\supermarkets-semi-colons.txt", sep=";") #loading text based files with semi colons
print(df5)


#setting header row in a data table

df8 = pandas.read_csv("data.txt", header = None) #used for fixing header values


#setting column names
df8.columns = ["ID", "Address", "City", "Zip", "Country", "Name", "Employees"]

#setting up index column
df9 = df8.set_index("ID")
df8.set_index("ID", inplace=True)
df8.set_index("Name", inplace=True, drop=False)


#manipulating data, deleting and adding data, indexing and slicing
df10 = pandas.read_csv("Data analysis with pandas\supermarkets-commas.txt") #loading text based files with commas
print(df10)
df10 = df10.set_index("Address")
df10.loc["735 Dolores St":"332 Hill St", "Country": "ID"]
df10.loc["332 Hill St", "Country"] #single cell
df10.loc[:, "Country"] #all rows under country
list(df10.loc[:, "Country"]) #puts items in a list
df10.iloc[1:3,1:3]



#Deleting columns and rows
df10.iloc[3, 1:4]
df10.drop["City", 1] 
df10.drop["332 Hill St", 0]
df10. drop(df10.columns[0:3], 1)
df10.columns



#updating and adding new columns

