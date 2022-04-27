N,M = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
cd = [list(map(int,input().split())) for _ in range(M)]
INF = 4*10**9+1

for i in range(N):
    ans,dist = 0,INF
    for j in range(M):
        if dist > abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1]):
            ans = j + 1
            dist = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
    print(ans)
