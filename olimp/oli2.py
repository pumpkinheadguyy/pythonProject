x = int(input())
y = int(input())
n = int(input())
c1 = n // (x + y)
c1 *= 2
c2 = n % (x + y)
if c2 == 0:
    print(c1)
elif c2 <= y:
    print(c1 + 1)
else:
    print(c1 + 2)
