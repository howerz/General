import time
import statistics

repeats=input("How many times should the loop repeat? : ")
countto=input("How high should the counter count? : ")

x=1
z=1

TimeValues=[]

#def average(TimeValues):
#    return sum(TimeValues)/len(TimeValues)

while z<=int(repeats):
    start_time=time.time()
    while x <= int(countto):
#        print(x)
        x=x+1
    y=(time.time()-start_time)
#    print(y / x)
#    print("time: "+str(z))
    TimeValues.append(float(y/x))
    x=1
    z=z+1
#average=average(TimeValues)
#print(TimeValues)
#print(sum(TimeValues))
#print(len(TimeValues))
print("On average, it took " + str(statistics.mean(TimeValues)) + " seconds to increment an integer by 1 when incrementing from 1 to " + countto + ", " + repeats + " times.")