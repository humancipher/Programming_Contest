from itertools import permutations

S = list(input())
P = list(permutations(S))
print(len(set(P)))
