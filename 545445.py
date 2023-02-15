import  numpy as np
import pandas as pd
a=pd.Series([3,1,2,45,4,6,4,7])
b=pd.Series([1,2,1,5,4,7,8,741,2])
print(a)
print(b)
#add  ========> adding 2 series
c=a.add(b)
print(c)

#substract
print(a.subtract(b))

#multiply
print(a.multiply(b))
#division
print(a.divide(b))