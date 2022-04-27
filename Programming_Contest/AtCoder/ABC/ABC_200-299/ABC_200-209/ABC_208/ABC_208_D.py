INF = 10**9

n,m = map(int,input().split())
ABC = list()
for _ in range(m):
    a,b,c = map(int,input().split())
    ABC.append([a-1,b-1,c])

D = [[INF] * n for _ in range(n)]
for a,b,c in ABC:
    D[a][b] = c
for i in range(n):
    D[i][i] = 0

ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            D[i][j] = min(D[i][j],D[i][k]+D[k][j])
            if D[i][j] != INF:
                ans += D[i][j]
print(ans)