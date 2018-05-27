import pandas as pd
import numpy as np
import time

numMin = []
numMax = []
numAvg = []
# Time series 11.00, 11:05, 11:10, 11:15, 11:20
ts = pd.date_range("11:00", "11:20", freq="5min")

for i in range(5):
   numMin.append(np.random.randint(1,high=3))
   numMax.append(np.random.randint(10,high=15))
   numAvg.append(np.random.randint(3,high=10))

df = pd.DataFrame({'time': ts, 'min': numMin, 'max': numMax, 'avg': numAvg})
print(df)
print(df.shape)
print(df['avg'])
print(df['avg'].min())
print(df['avg'].max())
print(df[(df['time'] > '2018-05-05 11:05:00')])
