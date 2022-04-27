N,C = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in range(N)]

D = dict()
for a,b,c in ABC:
    if a not in D:
        D[a] = c
    else:
        D[a] += c
    if b+1 not in D:
        D[b+1] = -c
    else:
        D[b+1] -= c

L = [[d,D[d]] for d in D]
L.sort(key = lambda x:x[0])

for i in range(len(L)-1):
    L[i+1][1] += L[i][1]

for i in range(len(L)):
    L[i][1] = min(L[i][1],C)

ans = 0
for i in range(len(L)-1):
    ans += (L[i+1][0] - L[i][0]) * L[i][1]

print(ans)
