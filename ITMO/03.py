jumpers = []
a = int(input())
for x in range(a):
    li = list(input())
    cent = li[0]
    nam = li[1] + ' ' + li[2]
    del li[0:3]
    jumps = []
    for y in range(len(li)):
        if li[y] != 'x':
            jumps.append(float(li[y]))
    jumpers.append(Result(cent, nam, jumps))

