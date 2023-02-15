#drop_duplicates() =====> for removing duplicate rows
import pandas as pd
lst=[[101,'vinay','k',27,'bigdata',100000],
     [102,'manu','j',20,'doctor',20000],
     [103,'rahul','m',23,'python',40000],
     [104,'kiran','l',30,'bigdata',38000],
     [102, 'manu', 'j', 20, 'doctor', 20000],
     [103, 'rahul', 'm', 23, 'python', 40000],
     [104, 'kiran', 'l', 30, 'bigdata', 38000]]

df=pd.DataFrame(lst)

df.columns=['id','fname','lname','age','prof','salary']
print(df)
df1=df.drop_duplicates()
print(df1)

#how to drop a column
#new df name=olddfname.drop(['colname'],axis=1)
df2=df.drop(['id','lname'],axis=1)   #======> etra values veel drop cheiyan patum
print(df2)