
from functools import reduce


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
orbits1 = [((x * y) * 3.14) for x, y in orbits if not x == y]
max_orbits1 = reduce(lambda a, b: a if (a > b) else b, orbits1)
orbits2 = [(x, y) for x, y in orbits if ((x * y) * 3.14) == max_orbits1]
print(*orbits2[0])




# планета от Дениса

# def find_farthest_orbit(arr):
#     return [i for i in arr if i[0] * i[1] == max([i[0] * i[1] for i in arr if i[0] != i[1]])]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
