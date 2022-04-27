H,W = map(int,input().split())
N = int(input())
a = list(map(int,input().split()))

b = [0 for _ in range(N)]
b[0] = a[0]
for i in range(N-1):
    b[i+1] = b[i] + a[i]

C = [[None for _ in range(W)] for _ in range(H)]

pt = 0
for i in range(N):
    for j in range(a[i]):
        s,t = pt // W,pt % W
        C[s][t] = i+1
        pt += 1

for i in range(H):
    if i % 2 == 1:
        for j in range(W//2):
            C[i][j],C[i][W-j-1] = C[i][W-j-1],C[i][j]

for i in range(H):
    print(" ".join(map(str,C[i])))
