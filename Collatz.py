proven = []
temp = []

for i in range(1,101):
    temp.append(i)
    while i != 1:
        if i in proven:
            break
        elif i % 2 == 0:
            i = i // 2
            temp.append(i)
        else:
            i = (i * 3) + 1
            temp.append(i)
    for y in temp:
        if y in proven:
            continue
        else:
            proven.append(y)
    temp = []    
proven.sort()
print(proven)
print(str("{:,}".format(len(proven))) + " numbers have been proven with the max number being " + str("{:,}".format(max(proven))))