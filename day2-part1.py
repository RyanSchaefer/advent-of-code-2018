boxes = open('day2.txt', 'r').readlines()
searcher = lambda x, i: any([True for letter in "abcdefghijklmnopqrstuvwxyz" if x.count(letter) == i])
twos = list(filter(lambda x: searcher(x, 2), boxes))
threes = list(filter(lambda x: searcher(x, 3), boxes))
print(len(threes) * len(twos))