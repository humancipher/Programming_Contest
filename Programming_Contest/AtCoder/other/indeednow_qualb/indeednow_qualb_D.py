n,c = map(int,input().split())
A = list(map(int,input().split()))
D = [[0] for _ in range(c)]
for i in range(n):
    D[A[i]-1].append(i+1)
for i in range(c):
    D[i].append(n+1)
Ans = [n*(n+1)//2] * c
for i in range(c):
    for j in range(len(D[i])-1):
        span = D[i][j+1] - D[i][j] - 1
        Ans[i] -= span * (span+1) // 2
for i in range(c):
    print(Ans[i])