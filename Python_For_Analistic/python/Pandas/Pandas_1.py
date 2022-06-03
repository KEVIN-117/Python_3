
import numpy as np
import pandas as pd
df1 = pd.DataFrame({'A':['A0','A1', 'A2','A3','A4'],
                    'B':['B0','B1', 'B2','B3','B4'],
                    'C':['C0','C1', 'C2','C3','C4'],
                    'D':['D0','D1', 'D2','D3','D4']})

df2 = pd.DataFrame({'A':['A0','A1', 'A2','A3','A4'],
                    'B':['B0','B1', 'B2','B3','B4'],
                    'C':['C0','C1', 'C2','C3','C4'],
                    'D':['D0','D1', 'D2','D3','D4']})
print(pd.merge(df1, df2, on=['A', 'C']))
print(df1)
print(df2)