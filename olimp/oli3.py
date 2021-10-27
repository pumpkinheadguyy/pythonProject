import math


x = int(input())
y = int(input())
n = int(input())
ports = []
for i in range(n):
    ports.append(int(input()))
simple_walk = abs(y - x)
p_to_x = []
p_to_y = []
for j in ports:
    p_to_x.append(abs(x - j))
    p_to_y.append(abs(y - j))
hard_walk = min(p_to_x) + min(p_to_y) + 1
print(min(simple_walk, hard_walk))
