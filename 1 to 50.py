import numpy as np
import pandas as pd
s=pd.Series([i for i in range(1,51)])
print(s)

#first 5 rows

#head function ======> first 5 rows prnt cheiyu

print(pd.Series(s.head()))
print(pd.Series(s.head(10)))
#tail ======> last 5
print(pd.Series(s.tail()))

