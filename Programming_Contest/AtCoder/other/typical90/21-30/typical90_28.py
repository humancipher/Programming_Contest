D = [[0 for _ in range(1001)] for _ in range(1001)]

n = int(input())
for _ in range(n):
    x0,y0,x1,y1 = map(int,input().split())
    D[x0][y0] += 1
    D[x0][y1] -= 1
    D[x1][y0] -= 1
    D[x1][y1] += 1

for i in range(1001):
    for j in range(1,1001):
        D[i][j] += D[i][j-1]

for j in range(1001):
    for i in range(1,1001):
        D[i][j] += D[i-1][j]

Ans = [0 for _ in range(n+1)]
for i in range(1001):
    for j in range(1001):
        Ans[D[i][j]] += 1

for i in range(1,n+1):
    print(Ans[i])
