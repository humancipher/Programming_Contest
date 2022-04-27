INF = 10**6

n,m = map(int,input().split())
D = [[INF] * n for _ in range(n)]
for i in range(n):
    D[i][i] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    D[a-1][b-1] = c
    D[b-1][a-1] = c

D2 = [[D[i][j] for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            D2[i][j] = min(D2[i][j],D2[i][k]+D2[k][j])
ans = 0
for i in range(n):
    for j in range(i+1,n):
        #元々の(i,j)のパスが最短経路で使われているなら(i,j)の最短パスは元のやつのはず
        if D[i][j] != INF and D[i][j] > D2[i][j]:
            ans += 1
print(ans)