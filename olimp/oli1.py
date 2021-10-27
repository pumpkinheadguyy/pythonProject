n = int(input())
k = int(input())
if n == k:
    print(0)
else:
    n = n / k
    count = 0
    count += 4 * (n - 1)
    n -= 2
    while n > 0:
        count += 4 * (2 * n - 1)
        n -= 2
    print(int(count * k))
