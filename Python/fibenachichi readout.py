import time
start_time=time.time()
x=1
y=1
count = 2
print(x)
print(y)
while x < 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
    z=x+y
    x=y
    y=z
    print(z)
    count=count+1
print(str(z)+" is number " +str(count)+ " of the febenachichi sequence")
print("%s seconds" % (time.time()-start_time))