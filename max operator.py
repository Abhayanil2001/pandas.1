#max =========>evaluvating function

#newdfname=olddfname.groupby('colname') ['colname'].max()
#here 2 collumns has different values
#each location max salary

import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/Temperature.unknown',sep=' ',header=None)
df.columns=['year','tem']
print(df)

df1=df.groupby('year') ['tem'].max().sort_values(ascending=False)
print(df1)

#min operator ======> newdfnmae=olddfname.groupby('colname)['colname].min()
#min temp per year
df2=df.groupby('year') ['tem'].min().sort_values()
print(df2)
#sum ===> total sum
df3=df.groupby('year')['tem'].sum().sort_values()             #============syntax should be same for all the evaluvating functions
print(df3)
#mean ========> average
df4=df.groupby('year')['tem'].mean().sort_values()
print(df4)