import time

repeats=input("How many times should the loop repeat? : ")

i=1
x="Fizz"
y="Buzz"
z=1

Start_Time = time.time()

while z<=int(repeats):
    while i<=100:
        if i%3==0 and i%5==0:
            print(x+y)
        elif i%3==0:
            print(x)
        elif i%5==0:
            print(y)
        else:
            print(i)
        i+=1
    z+=1
    i=1
print("It took " + str(time.time()-Start_Time) + "seconds to run FizzBuzz " + repeats + " times. That is " + str((time.time()-Start_Time)/int(repeats)) + "ms per cycle.")