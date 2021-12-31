import matplotlib.pyplot as plt

proven = set()
temp = set()

for i in range(1,50_001):
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

plt.plot(list(proven))
plt.ylabel('numbers')
plt.xlabel('inc')
plt.show()