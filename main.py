import pandas as pd
import numpy as np

df = pd.read_csv("apartemen2.csv")

print(df)
print(20*"=")

print(df.isnull().values.any())
print(20*"=")

print(df.isnull().sum().sum())
print(20*"=")

print(df['KodeApt'])
print(20*"=")
print(df['KodeApt'].isnull())
print(20*"=")

print(df['Jum_kamar'])
print(20*"=")
print(df['Jum_kamar'].isnull().sum())
print(20*"=")

missing_values = ["n/a", "na", "--","benar"]
df = pd.read_csv("apartemen2.csv", na_values=missing_values)
print(df['Jum_kamar'])
print(20*"=")

print(df['Jum_kamar'].isnull())
print(20*"=")

# df['St_Milik']
# df['St_Milik'].isnull()

# #deteksiangka
index = 0
for row in df['St_Milik']:
    try:
        df['St_Milik'].isnull()
        int(row)
        df.loc[index, 'St_Milik']=np.nan
    except ValueError:
        pass
    index+=1

print(df['St_Milik'].isnull())
# df.isnull().sum().sum()