import time
Start_Time = time.time()

Keywords = {3:"Fizz", 5:"Buzz"}

for i in range(1, 1_001):
    Output = ""
    for x in Keywords:
        if i % x == 0:
            Output += Keywords[x]
    if Output == "":
        Output = i
    print(Output)

print(time.time()-Start_Time)