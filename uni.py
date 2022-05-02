import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[7,1,5,4,2,1,4,4,8],'B':[1,2,8,5,3,4,2,6,8]})

print(df)
print(df['A'].unique())
print(type(df['A'].unique()))