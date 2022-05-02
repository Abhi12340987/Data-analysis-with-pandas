import pandas


df1 = pandas.read_csv("Data analysis with pandas\supermarkets.csv") #loading csv file using pandas and python


df1["Continent"] = df1.shape[0]*["North America"]

df1["Continent"] = df1["Country"] + ", " + "North America"

print(df1) 

df1_t=df1.T #transpose of data table, rows become comlumns and vice versa
#print(df1_t)

#df1_t["My Address"] = ["My City", "My Country", 10, 7, "My Shop", "My State", "My Continent"]
print(df1_t)

#df1 = df1_t.T #the added column gets converted to a row






df2 = pandas.read_csv("Data analysis with pandas\supermarkets.csv") #loading csv file using pandas and python


df2["Continent"] = df2.shape[0]*["North America"]

df2["Continent"] = df2["Country"] + ", " + "North America"

print(df2) 

df2_t=df2.T #transpose of data table, rows become comlumns and vice versa
#print(df1_t)

#df2_t["My Address"] = ["My City", "My Country", 10, 7, "My Shop", "My State", "My Continent"]
print(df2_t)

#df2 = df2_t.T #the added column gets converted to a row

dm = pandas.merge(left=df1,right=df2,on="ID")

from geopy.geocoders import ArcGIS
nom = ArcGIS()
n = nom.geocode("3995 23rd, St, San Francisco, CA 94114")
print(n)
print(n.latitude)
print(n.longitude)

df = pandas.read_csv("Data analysis with pandas/supermarkets.csv")
print(df)
df["Address"] = df["Address"]+"," +df["City"]+"," +df["State"]+ "," +df["Country"]
print(df) #Creates a columns for address with a complete address string


df["Coordinates"] = df["Address"].apply(nom.geocode)
print(df)

print(df.Coordinates[0].latitude)

df["Latidude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)
#from geopy.geocoders import Nominatim
#nom = Nominatim()
#Geocoding means converting from addresses to coordinates

