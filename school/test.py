data = []
end = 0
with open("data.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()][0])
    for i in data:
        if i > end:
            if i % 7 == 0:
                end = i
    print(end)
