import pandas as pd

df=pd.read_csv('C:/Users/Dell/Documents/.unknown',sep=',',header=None)
df.columns=(['fname','lname','age','profressiojn','location'])
print(df)

#how to collect new columns
df1=df[['fname','lname','age']]
print(df1)
