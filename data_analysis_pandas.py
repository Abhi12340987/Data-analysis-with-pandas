import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price", "Age", "Value"],index=["First", "Second"])

print(df1)

df2 = pandas.DataFrame([{"Name":"John", "surname":"parker"}, {"Name":"Jack", "surname":"brown"}])
print(df2)

print(df1.mean())