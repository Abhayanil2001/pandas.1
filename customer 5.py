#customer 5  complete using evaluating functions
#1 find total number of rows
#2 each profession count decending order
# 3 each country count
 #4 each prof max salery
 #5 each country min salary
 #6 each prof total salary
 #7each prof average salary
 #8 each prof min age

import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/customer5.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','profession','country','salary']
print(df)
print('*'*100)

#1
df9=len(df)
print(df9)


#2
df1=df.groupby('profession')['profession'].count().sort_values()
print(df1)
#3
df2=df.groupby('country')['country'].count().sort_values()
print(df2)
#4
df3=df.groupby('profession')['salary'].max().sort_values()
print(df3)
#5
df4=df.groupby('country')['salary'].min().sort_values()
print(df4)
#6
df5=df.groupby('profession')['salary'].sum().sort_values()
print(df5)
#7
df6=df.groupby('profession')['salary'].mean().sort_values()
print(df6)
#8
df7=df.groupby('profession')['age'].min().sort_values()
print(df7)