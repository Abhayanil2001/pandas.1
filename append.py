import numpy as np
import pandas as pd
a=pd.Series([1,2,3,6])
b=pd.Series([6,4,5,8,5])
print(a)
print(b)
#append
print(pd.Series(a.append(b,ignore_index=True)))