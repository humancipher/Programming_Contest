INF = 10**15
n,m = map(int,input().split())
D = [[INF] * n for _ in range(n)]
G = [[INF] * n for _ in range(n)]
G2 = [[INF] * n for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c
    D[a-1][b-1] = c
    D[b-1][a-1] = c
    G2[a-1][b-1] = c
    G2[b-1][a-1] = c

for i in range(n):
    G[i][i] = 0
    D[i][i] = 0
    G2[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if D[i][j] >= D[i][k] + D[k][j] and i != k and k != j:
                D[i][j] = D[i][k] + D[k][j]
                if G[i][j] != INF:
                    G[i][j] = INF
ans = 0
for i in range(n):
    for j in range(n):
        if G[i][j] != G2[i][j]:
            ans += 1
print(ans//2)