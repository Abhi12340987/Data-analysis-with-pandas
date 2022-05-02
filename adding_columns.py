import pandas


df1 = pandas.read_csv("Data analysis with pandas\supermarkets.csv") #loading csv file using pandas and python


df1["Continent"] = df1.shape[0]*["North America"]

df1["Continent"] = df1["Country"] + ", " + "North America"

print(df1) 

df1_t=df1.T #transpose of data table, rows become comlumns and vice versa
#print(df1_t)

df1_t["My Address"] = ["My City", "My Country", 10, 7, "My Shop", "My State", "My Continent"]
print(df1_t)

df1 = df1_t.T #the added column gets converted to a row

