import time

start = time.perf_counter()

proven = set()
temp = set()

for i in range(1,10_001):
    temp.add(i)
    while i != 1:
        if i in proven:
            break
        elif i % 2 == 0:
            i = i // 2
            temp.add(i)
        else:
            i = (i * 3) + 1
            temp.add(i)
    proven = proven.union(temp)
    temp.clear()    
#print(proven)
#print(str("{:,}".format(len(proven))) + " numbers have been proven with the max number being " + str("{:,}".format(max(proven))))

total = time.perf_counter() - start
print(total)
print(len(proven))