import string
from functools import reduce
s = open("day5.txt", 'r').read()

def destroy(sofar, xi):
    if sofar == '':
        return xi
    if sofar[-1] in string.ascii_uppercase:
        if sofar[-1].lower() == xi:
            return sofar[:-1]
    if sofar[-1] in string.ascii_lowercase:
        if sofar[-1].upper() == xi:
            return sofar[:-1]
    return sofar+xi

print(min([len(reduce(destroy, s.replace(l, "").replace(l.upper(), ""))) for l in string.ascii_lowercase]))