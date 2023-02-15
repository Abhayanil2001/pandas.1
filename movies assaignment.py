#assaignment
import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/movies_cleaned_new.csv',sep=',')
print(df)
#1. Find row count
print('number of rows',len(df))
#2 . Remove duplicates and find row count
df1=df.drop_duplicates()
print(df1)
#6.. Find Each year release movie count [count desc order]
df2=df.groupby('year') ['year'].count().sort_values(ascending=False)
print(df2)
#3.. Sort data set by release year in des order
df3=df.sort_values(by='year',ascending=False)
print(df3)
#4 Find rating mxm 5 movies name,year,rating
df4=df.sort_values(by='rating',ascending=False)[['name','year','rating']].head(5)
print(df4)
# 5. Find rating minimum 3 movies name,year,rtaing
df5=df.sort_values(by='rating',ascending=False)[['name','year','rating']].tail(3)
print(df5)
# 7. Each rating count [count desc order]
df6=df.groupby('rating')['rating'].count().sort_values(ascending=False)
print(df6)
# 8. 2008 and rating above 3 [collect]
# A. row count
df7=df.loc[(df['year']==2008)&(df['rating']>=3)]
print(df7)
print(len(df7))

# 9. Find duration mxm 1 movies name,year,rating,duration
df8=df.groupby('name')[['year','rating','duration']].max().sort_values(by='duration',ascending=False).head(1)
print(df8)
# 10. Find rating mnm 1 movies name,year,rating,duration
df9=df.groupby('name')[['year','rating','duration']].min().sort_values(by='rating',ascending=True).head(1)
print(df9)
# 11. Rating above 4 and relase year above 2005
# A. Rating mxm movies full data
# B. Rating mnm movies full data
df10=df.loc[(df['rating']>=4)&(df['year']>=2005)]
print(df10)
#A
df11=df10.groupby('name')[['year','rating','duration']].max().sort_values(by='rating',ascending=False)
print(df11)
#B
df12=df10.groupby('name')[['year','rating','duration']].min().sort_values(by='rating',ascending=True)
print(df12)
# 12. 2008 movies count
df13=df.loc[df['year']==2008]['year'].count()
print(df13)
# 13. 1975-2000 movies collect
# A. Row count
df14=df.loc[(df['year']>=1975) &(df['year']<=2000)][['name']]
print(df14)
print(len(df14))
# 14. 1975-2000 and rating above 3.5 total row count
df15=df.loc[(df['year']>=1975) &(df['year']<=2000) & (df['rating']>3.5)]
print(df15)
print(len(df15))