#filter ===========> loc function

#conditions accept cheiyuna datas matram accept cheiyum
#synatx
#newdataframename=olddfname.loc[dfname['columnname']condition]
import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/.unknown',sep=',',header=None)
df.columns=(['id','fname','lname','age','profession','country'])
print(df)

df1=df.loc[df['age']>58] [['fname','lname','age']]
print(df1)