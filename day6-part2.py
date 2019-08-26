inp = list(map(lambda x: tuple(int(y) for y in x.strip("\n").split(", ")), open("day6.txt").readlines()))
mins = [min(inp, key=lambda x: x[0])[0],
          min(inp, key=lambda x: x[1])[1]]
inp = list(map(lambda x: (x[0] - mins[0], x[1] - mins[1]), inp))
maxes = [max(inp, key=lambda x: x[0])[0], max(inp, key=lambda x: x[1])[1]]
m = []
for x in range(maxes[0]):
    m.append([])
    for y in range(maxes[1]):
        print(x,y)
        m[x].append(0)

for point in inp:
    for x in range(maxes[0]):
        for y in range(maxes[1]):
            m[x][y] += abs(point[0] - x) + abs(point[1] - y)

for x in range(maxes[0]):
    m[x] = list(filter(lambda x: x < 10000, m[x]))

total = 0
for x in range(maxes[0]):
    total += len(m[x])

print(total)
