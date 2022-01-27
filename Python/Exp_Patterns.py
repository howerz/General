### Numbers get too large that default settings cannot handle the float
### Times are too small that default settings cannot handle the float

import time

x=5
y=5
Counter=1
Times=[]

#print(y)

while Counter<=5:
    start=time.time()
    y=(y**x)
    Times.append(time.time() - start)
#    print(str(Counter) + "   " + str(y))
#    print(str(time.time() - start)+ " seconds.")
    Counter+=1
print(y)
print(Times)