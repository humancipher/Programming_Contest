N = int(input())
APX = [list(map(int,input().split())) for _ in range(N)]

INF = 1 << 60
ans = INF
for a,p,x in APX:
    if (x-a) > 0:
        ans = min(ans,p)
if ans != INF:
    print(ans)
else:
    print(-1)
