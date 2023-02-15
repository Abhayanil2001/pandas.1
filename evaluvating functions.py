#evaluvating functions
#count
#sum
#max
#min
#mean

#count   ===========>finding corroseponding colums count

#group function=====> group cheith matra evaluavate cheiyan patu so first group

#newdfnname=olddfname.groupby('colname')['colname].count()
import  numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/.unknown',sep=',',header=None)
df.columns=['id','fname','lname','age','profession','location']
print(df)
#each profession count
df1=df.groupby('profession') ['profession'].count().sort_values(ascending=False)
print(df1)

#each country count[des order]
df2=df.groupby('location') ['location'].count().sort_values(ascending=False)
print(df2)
df3=df.groupby('age')['age'].count().sort_values()
print(df3)