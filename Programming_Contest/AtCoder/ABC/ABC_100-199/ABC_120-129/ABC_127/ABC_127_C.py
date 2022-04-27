N,M = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(M)]
INF = 10**5+1

small,big = 0,INF
for i in range(M):
    small = max(small,LR[i][0])
    big = min(big,LR[i][1])

if small <= big:
    print(big-small+1)
else:
    print(0)
