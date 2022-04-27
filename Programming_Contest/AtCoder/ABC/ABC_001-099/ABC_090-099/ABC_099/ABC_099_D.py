INF = 10**10

n,c = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(c)]
C = [list(map(int,input().split())) for _ in range(n)]

T = [[0] * c for _ in range(3)]
for i in range(n):
    for j in range(n):
        k = (i+j) % 3
        T[k][C[i][j]-1] += 1

ans = INF
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i != j and j != k and k != i:
                tmp = 0
                for s in range(c):
                    tmp += T[0][s] * D[s][i]
                    tmp += T[1][s] * D[s][j]
                    tmp += T[2][s] * D[s][k]
                ans = min(ans,tmp)
print(ans)
