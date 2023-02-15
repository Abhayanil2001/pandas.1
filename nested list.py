#nested list
#id,fname,lname,age,prof,salary
import pandas as pd
lst=[[101,'sugu','k',55,'kooli',100000],
     [102,'ramu','ma',35,'kallan',1000000000],
      [103,'soman','kp',62,'analyst',10000]]
df=pd.DataFrame(lst)
df.columns=['emp_id','fname','lname','age','prof','salary']
print(df)
print(df.head())
print(df.tail())
print(df.size)
print(df.shape)

#printing the colmns in a data set
print(df.columns)

print('*'*100)
#discribe()
print(df.describe())

#include
print(df.describe(include='O'))     #here objects are dicribed
print(df.describe(include='all'))
#NaN not a number

###################################################################################################################
#how to add new columns
df['gender']=['M','F','F']
print(df)

df['status']=['single','married','single']
print(df)

df['experience']=[1,2,5]
print(df)


#how to collect new columns
df1=df[['fname','lname','age']]
print(df1)

#filter
df1=df.loc[df['age']>28] [['fname','lname','age']]
print(df1)
