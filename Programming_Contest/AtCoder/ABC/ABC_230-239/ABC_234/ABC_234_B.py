from math import sqrt

def dist(x0,y0,x1,y1):
    return sqrt((x0-x1)**2 + (y0-y1)**2)

n = int(input())
XY = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans = max(ans,dist(XY[i][0],XY[i][1],XY[j][0],XY[j][1]))
print(ans)