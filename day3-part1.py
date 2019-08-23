import re
claims = open("day3.txt", 'r').read()
claims = re.findall("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", claims)

m = []
for x in range(1000):
    m.append([])
    for y in range(1000):
        m[x].append(0)

def process_match(match):
    match = list(map(int, match))
    return [(match[1]-1, match[2]-1), # top right
            (match[1] + match[3] -1, match[2] + match[4]-1)] # bottom left

def paint_map(coords, map):
    for x in range(coords[0][0], coords[1][0]):
        for y in range(coords[0][1], coords[1][1]):
            map[x][y] += 1
    return map


for claim in claims:
    m = paint_map(process_match(claim), m)

sqft = 0
for row in m:
    sqft += len(list(filter(lambda x: x > 1, row)))

print(sqft)
