
import copy

a = [11,22,33]
b = [44,55]

c = (a,b)

d = copy.copy(c)

c[0].append(44)

print(d[0])

