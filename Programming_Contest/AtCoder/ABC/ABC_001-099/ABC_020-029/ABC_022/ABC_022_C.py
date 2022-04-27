INF = 10**8
n,m = map(int,input().split())
A = [[INF] * n for _ in range(n)]
B = [[INF] * n for _ in range(n)]
for i in range(n):
    A[i][i] = 0
    B[i][i] = 0

for _ in range(m):
    u,v,l = map(int,input().split())
    u,v = u-1,v-1
    if u == 0 or v == 0:
        B[u][v] = l
        B[v][u] = l
    else:
        A[u][v] = l
        A[v][u] = l

for k in range(n):
    for i in range(1,n):
        for j in range(1,n):
            A[i][j] = min(A[i][j],A[i][k]+A[k][j])

ans = INF
for i in range(1,n):
    for j in range(1,n):
        if i != j:
            ans = min(ans,B[0][i]+A[i][j]+B[j][0])
if ans != INF:
    print(ans)
else:
    print(-1)
