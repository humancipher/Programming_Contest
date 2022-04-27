from collections import Counter

S = list(input())

C = Counter(S)
MC = C.most_common()

print(MC[0][0])
