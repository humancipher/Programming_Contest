from bisect import bisect_right
from copy import copy

N = int(input())
ABCD = [list(map(int,input().split())) for _ in range(N*(N-1)//2)]

T = [0 for i in range(N)]

for a,b,c,d in ABCD:
    if c < d:
        T[b-1] += 3
    elif c > d:
        T[a-1] += 3
    else:
        T[a-1] += 1
        T[b-1] += 1

U = copy(T)
U.sort()

for i in range(N):
    print(N - bisect_right(U,T[i]) + 1)
