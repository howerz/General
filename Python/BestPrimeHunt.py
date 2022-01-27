def is_prime_number(x):
    z = 0
    for i in str(x):
        z += int(i)
    if z % 9 == 0:
        return "Not Prime"
    else:
        for y in range(2,int(x)//2+1):
            if not ( int(x) % y ):
                return "Not Prime"
            else:
                pass
    return "Prime"


x=10
p = ''
for i in range(1,x+1):
    p += str(i)
p = p + p[len(p)-len(str(x))-1::-1]
print(p)
print("{:,}".format(len(p)))
print(is_prime_number(p))
