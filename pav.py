import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import csv
import sklearn

csv_path='Retail.csv'
df=pd.read_csv(csv_path, nrows=200)
df.head()
df_new = df.iloc[:, [0,1,3,4,5,6,7]]
df_new= pd.DataFrame(df_new)
print(df_new)
print("-----------------------------------------------------------------")


ci=int(input("Enter Your Customer Id: "))
td = input("Enter date: \n >> ")


cd=df_new.groupby('Country')['CustomerID'].count()
print(cd)
print("-----------------------------------------------------------------")


uk=df[df['Country'] == 'United Kingdom'].groupby("CustomerID")["Quantity"].sum()
z=df[df['CustomerID'] == ci]['Quantity'].sum()
tc=df["TotalPrice"] = df['Quantity'] * df['UnitPrice']
tc=df[df['CustomerID'] == ci]["TotalPrice"].sum()
print(uk)
print("-----------------------------------------------------------------")

fr=df[df['Country'] == 'France'].groupby("CustomerID")["Quantity"].sum()
y=df[df['CustomerID'] == ci]["Quantity"].sum()
tc=df["TotalPrice"] = df['Quantity'] * df['UnitPrice']
tc=df[df['CustomerID'] == ci]["TotalPrice"].sum()
print(fr)
print("-----------------------------------------------------------------")

au=df[df['Country'] == 'Australia'].groupby("CustomerID")["Quantity"].sum()
x=df[df['CustomerID'] == ci]["Quantity"].sum()
tc=df["TotalPrice"] = df['Quantity'] * df['UnitPrice']
tc=df[df['CustomerID'] == ci]["TotalPrice"].sum()
print(au)
print("-----------------------------------------------------------------")


if ci in uk:
    print("This Customer Is From The UK And Has A Budget Of  :$",tc)
    print("Please Refer To The Recommendations.csv File To View Our Recommendations That Fall In Your Budget ")
elif ci in fr:
    print("This Customer Is From France And Has A Budget Of  :$",tc)
    print("Please Refer To The Recommendations.csv File To View Our Recommendations That Fall In Your Budget ")
elif ci in au:
    print("This Customer Is From Australia And Has A Budget Of :$",tc)
    print("Please Refer To The Recommendations.csv File To View Our Recommendations That Fall In Your Budget ")
    
df_new1=df.iloc[:,[2,4,6]]
df_new1=df_new1[df_new1['CustomerID'] == ci]
df_new1=pd.DataFrame(df_new1)
df_new1=df_new1.to_csv('recommendations.csv', index=False)


csv_path='recommendations.csv'
df=pd.read_csv(csv_path, nrows=200)
df.head()
df_new = df.iloc[:, [1,2,3]]
df_new= pd.DataFrame(df_new)
print(df_new)
print("-----------------------------------------------------------------")









    

