#customer file
#1 fname lname age loc [data frame]
#2.find total number of missing values
#3.missing values filled by india
#4.india fname lname age prof
#5 india work and age above 40 fname lname age prof
#6 us data collect
#7 us work  age max 5 empolyee fname lanmae age  prof
#8 india work age min 3 employee fname lname age prof
#9 uk work age range between 25 to 35
#10 australia age max 1 employee fu;ll data
#11 piolet prof age max 1 empolyee fnmae lname age loc
#12 us and prof musican age max1 employee ful data

import  numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/.unknown',sep=',',header=None)
df.columns=['id','fname','lname','age','profession','location']
print(df)

#1.
df1=[['fname','lname','age','location']]
print(df1)

#2.
print(df.isna().sum())

#3.
df2=df.fillna('India')
print(df2)
print(df2.isna().sum())
#4.
df3=df.loc[df['location']=='india'][['fname','lname','age','profession']]
print(df3)
#5
df4=df.loc[(df['location']=='india')&(df['age']>40)][['fname','lname','age','profession']]
print(df4)
#6
df5=df.loc[df['location']=='us']
print(df5)
#7
df6=df.loc[df['location']=='us'].sort_values(by='age')[['fname','lname','age','profession']].tail(5)
print(df6)
#8
df7=df.loc[df['location']=='india'].sort_values(by='age')[['fname','lname','age','profession']].tail(3)
print(df7)
#9
df8=df.loc[(df['location']=='uk')&(df['age'])>=25 & (df['age']<=35)][['fname','lname','age','profession']]
print(df8)
#10
df9=df.loc[df['location']=='australia'].sort_values(by='age').tail(1)
print(df9)
#11
df10=df.loc[df['profession']=='Piolet'].sort_values(by='age')[['fname','lname','age','location']].tail(1)
print(df10)
#12
df11=df.loc[(df['location']=='us')&(df['profession']=='Musican')].tail(1)
print(df11)