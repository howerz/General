Numbers = []

for i in range(1,5000):
    Numbers.append(i)
#    print(i)
    while i != 1:
        if i % 2 == 0:
            i = i / 2
        else:
            i = (i * 3) + 1
#        if i == 1:
#            print(i)
#            print("Done.")
#        else:
#            print(i)
print(Numbers)