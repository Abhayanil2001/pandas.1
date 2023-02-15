#sort
#ascending order
#decendiing ordeer

#newdfname=olddfnmae.sort_values(by='colname')

import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/sample4.txt',sep=',',header=None)

df.columns=(['id','fname','lname','age','phno','location'])
print(df)

#sort
df1=df.sort_values(by='age')     #======> ascending order
print(df1)

#
df2=df.sort_values(by='age',ascending=False) #==========>decending order
print(df2)

df3=df.sort_values(by='fname') #============> object also been soarted in the formate of alfabetting order
print(df3)

#1 age max 1 emoployee fname,lame,age,loc
#2. age minimum 2 employee fname,lname,age,phno
#3. chennai work age max 1 employee fname lname age phno
#1
df4=df.sort_values(by='age',ascending=False)  [['fname','lname','age','location']].head(1)
print(df4)
#2
df5=df.sort_values(by='age')  [['fname','lname','age','phno']].head(2)
print(df5)
#3
#loc,sort,col,head/tail   =======> proper format
df6=df.loc[df['location']=='chennai'].sort_values(by='age') [['fname','lname','age','phno']].head(1)
print(df6)