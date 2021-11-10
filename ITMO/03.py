class Result:
    def __init__(self, cent, nam, jumps):
        self.cent = cent
        self.nam = nam
        self.jumps = jumps


jumpers = []
a = int(input())
for x in range(a):
    li = input().split(' ')
    cent = li[0]
    nam = li[1] + ' ' + li[2]
    del li[0:3]
    jumps = []
    for y in range(len(li)):
        if li[y] != 'x':
            jumps.append(li[y])
    jumpers.append(Result(cent, nam, jumps))
    jumps = []
print(jumpers, jumpers[0].cent, jumpers[0].nam, end=', ')

