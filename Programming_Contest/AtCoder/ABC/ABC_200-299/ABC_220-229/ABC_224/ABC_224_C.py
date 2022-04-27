n = int(input())
XY = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (XY[k][0]-XY[i][0]) * (XY[j][1]-XY[i][1]) != (XY[j][0]-XY[i][0]) *(XY[k][1]-XY[i][1]):
                ans += 1
print(ans)
