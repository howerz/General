import time

i=1
x="Fizz"
y="Buzz"

Start_Time = time.time()

while i<=1_000:
    if i%3==0 and i%5==0:
        print(x+y)
    elif i%3==0:
        print(x)
    elif i%5==0:
        print(y)
    else:
        print(i)
    i+=1
i=1
print(time.time()-Start_Time)