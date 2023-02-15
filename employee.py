import numpy as np
import  pandas as pd
dic={'id':101,'fname':'vinay','lname':'k p','age':25,"prof":'data scientist','salary':100000000}
a=pd.Series(dic,index=['fname','lname','salary','prof','age'])
print(a)

#order change cheith varan ==========> index


####################################
import pandas as pd
a=pd.Series([4,5,6,1,2,35,6,5,8,9],index=[2,0,6,4,5,4,7,9,3,8])
print(a)
#here index matra maru no values has been changed yet