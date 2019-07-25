import itertools
data = [1,2,2]

permutations = itertools.permutations(data)

sets = set(permutations)
#print(permutations)
print(list(sets))
