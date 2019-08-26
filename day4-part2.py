import re
import datetime
from functools import reduce
text = open("day4.txt", 'r').read()
guards = re.findall("\[(.+)\] Guard #(\d+) begins shift", text)
dates = re.findall("\[(.+)\] (wakes up|falls asleep)", text)

guards = list(
    map(lambda x: [(datetime.datetime.strptime(x[0], "%Y-%m-%d %H:%M") + datetime.timedelta(hours=1)).date(),
                   x[1]], guards))
guards = {x[0]: {"id": x[1], "sleep": [], "shift": [0 for y in range(60)]} for x in guards}

dates = list(map(lambda x: [datetime.datetime.strptime(x[0], "%Y-%m-%d %H:%M"), x[1]], dates))

for date in dates:
    guards[date[0].date()]["sleep"].append(date)

print(guards)
for date in guards:
    guards[date]["sleep"].sort(key=lambda x: x[0])
    i = 0
    last = "wakes up"
    for x in range(60):
        if not guards[date]["sleep"]:
            guards[date]["shift"][i:] = [1 if last == "falls asleep" else 0 for x in range(x, 60)]
            break
        if x == guards[date]["sleep"][0][0].minute:
            last = guards[date]["sleep"][0][1]
            guards[date]["shift"][i-1:x] = [0 if last == "falls asleep" else 1 for x in range(i-1, x)]
            i = x+1
            del guards[date]["sleep"][0]

group_by_id = {}
for date in guards:
    if guards[date]["id"] not in group_by_id.keys():
        group_by_id.update({guards[date]["id"]: [guards[date]["shift"]]})
    else:
        group_by_id[guards[date]["id"]].append(guards[date]["shift"])

group_by_id = dict(
    map(lambda key: (key, reduce(lambda x, y: [a+b for a,b in zip(x, y)], group_by_id[key])),
        group_by_id.keys()))
sums = dict(map(lambda key: (key, sum(group_by_id[key])), group_by_id.keys()))
maxes = dict(map(lambda key: (key, max(group_by_id[key])), group_by_id.keys()))

for id in group_by_id:
    print(len(group_by_id[id]))
id = max(maxes.items(), key=lambda x: x[1])[0]
print(id, group_by_id[id].index(maxes[id]))