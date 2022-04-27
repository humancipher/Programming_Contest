N,D = map(int,input().split())
XY = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    x,y = XY[i][0],XY[i][1]
    if x**2 + y**2 <= D**2:
        cnt += 1

print(cnt)
