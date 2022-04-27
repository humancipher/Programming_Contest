from itertools import accumulate
from collections import Counter

N = int(input())
A = list(map(int,input().split()))

A = list(accumulate(A))

C = Counter(A)

ans = 0
for c in C:
    if c != 0:
        ans += C[c] * (C[c] - 1) // 2
    else:
        ans += C[c] * (C[c] - 1) // 2
        ans += C[c]

print(ans)
