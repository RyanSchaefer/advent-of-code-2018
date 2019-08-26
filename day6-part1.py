inp = list(map(lambda x: tuple(int(y) for y in x.strip("\n").split(", ")), open("day6.txt").readlines()))
mins = [min(inp, key=lambda x: x[0])[0],
          min(inp, key=lambda x: x[1])[1]]
# make inp zero based
inp = list(map(lambda x: (x[0] - mins[0], x[1] - mins[1]), inp))
maxes = [max(inp, key=lambda x: x[0])[0], max(inp, key=lambda x: x[1])[1]]
m = []
for x in range(maxes[0]):
    m.append([])
    for y in range(maxes[1]):
        m[x].append([])

for point in inp:
    for x in range(maxes[0]):
        for y in range(maxes[1]):
            m[x][y].append([point, abs(point[0] - x) + abs(point[1] - y)])

def min_or_none(l):
    return list(filter(lambda x: x[1] == min(l, key=lambda x: x[1])[1], l))

for x in range(maxes[0]):
    for y in range(maxes[1]):
        m[x][y] = min_or_none(m[x][y])

banned = []
for x in range(maxes[0]):
    try:
        banned.append(m[x][0][0][0]) if len(m[x][0]) == 1 else None
        banned.append(m[x][-1][0][0]) if len(m[x][-1]) == 1 else None
    except:
        break

for y in range(maxes[1]):
    banned.append(m[0][y][0][0]) if len(m[0][y]) == 1 else None
    banned.append(m[-1][y][0][0]) if len(m[-1][y]) == 1 else None

counter = {}
for x in range(maxes[0]):
    for y in range(maxes[1]):
        if len(m[x][y]) == 1:
            close = m[x][y][0][0]
            if close not in banned:
                if close not in counter.keys():
                    counter.update({close: 1})
                else:
                    counter[close] += 1

print(max(counter.items(), key=lambda x: x[1]))