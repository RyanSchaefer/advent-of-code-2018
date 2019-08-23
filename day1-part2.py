changes = open("day1.txt", 'r').readlines()
changes = list(map(int, changes))
seen = set()
seen.add(0)
last_sum = 0
i = 0
while 1:
    last_sum = last_sum + changes[i % len(changes)]
    if last_sum in seen:
        break
    seen.add(last_sum)
    i += 1
print(last_sum)