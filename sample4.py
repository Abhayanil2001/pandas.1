#1fname lname age loc
#2 age above 22 dat
#3.age equal to 24 fname,lname,phno
#4.chennai eork fnmae,lnmae,age phno
import numpy as np
import pandas as pd

df=pd.read_csv('C:/Users/Dell/Documents/sample4.txt',sep=',',header=None)

df.columns=(['id','fname','lname','age','phno','location'])
print(df)
#1
df1=df[['fname','lname','age','location']]
print(df1)
#2
df2=df.loc[df['age']>22]
print(df2)
#3
df3=df.loc[df['age']==24] [['fname','lname','phno']]
print(df3)
#4.
df4=df.loc[df['location']=='chennai'] [['fname','lname','age','phno']]
print(df4)

#more than one condition
#newdfnmae=olddfname.loc[df('colnmae']condition)&(df['colnmae']condition)
print('*'*1000)
#
# df5=df.loc[df['location']=='chennai']&(df['age']==24) [['fname','lname','age','phno']]
# print(df5)  ##====> clear the error
#combination of two statements
df5 = df.loc[(df['location'] == 'chennai') & (df['age'] == 24)][['fname', 'lname', 'age', 'phno']]
print(df5)

