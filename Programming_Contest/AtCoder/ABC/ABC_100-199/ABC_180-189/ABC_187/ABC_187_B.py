N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1,N):
        if xy[i][0] != xy[j][0]:
            if abs(xy[j][1] - xy[i][1]) <= abs(xy[j][0] - xy[i][0]):
                ans += 1

print(ans)
