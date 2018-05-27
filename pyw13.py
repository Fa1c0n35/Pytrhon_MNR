import numpy as np
import time

numMin = []
numMax = []
numAvg = []
ts = []

tformat = "%d/%m/%Y"
print(time.strftime(tformat))
tformat = "%H:%M"
#tformat = "%H:%M:%S"
for i in range(5):
   numMin.append(np.random.randint(1,high=3))
   numMax.append(np.random.randint(10,high=15))
   numAvg.append(np.random.randint(3,high=10))
   ts.append(time.strftime(tformat))
   print("!",end='',flush=True)
   time.sleep(60)
print('')
for i in range(5):
   print(ts[i],"Min:",numMin[i],"Max:",numMax[i],"Average:",numAvg[i])
