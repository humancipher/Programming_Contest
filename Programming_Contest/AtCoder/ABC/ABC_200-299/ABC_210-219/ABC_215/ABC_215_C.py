from itertools import permutations

S,k = list(input().split())
S = list(S)
k = int(k)
SP = set()
for sp in list(permutations(S)):
    SP.add("".join(sp))
SP = list(SP)
SP.sort()
print(SP[k-1])
