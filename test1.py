import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inilne

RandList=[]

for y in range(1_000):
    x=random.randint(1,100)
    RandList.append(x)
#print(RandList)

df = pd.DataFrame(RandList, columns=['Number'])
print(df)

df.plot