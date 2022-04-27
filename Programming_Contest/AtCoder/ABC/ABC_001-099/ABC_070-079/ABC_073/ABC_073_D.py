from itertools import permutations

INF = 10**8
n,m,r = map(int,input().split())
R = list(map(int,input().split()))
for i in range(r):
    R[i] -= 1
PR = list(permutations(R))
D = [[INF] * n for _ in range(n)]
for i in range(n):
    D[i][i] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    D[a-1][b-1] = c
    D[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            D[i][j] = min(D[i][j],D[i][k]+D[k][j])

ans = INF
for pr in PR:
    tmp = 0
    for i in range(len(pr)-1):
        tmp += D[pr[i]][pr[i+1]]
    ans = min(ans,tmp)
print(ans)
