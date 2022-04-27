def judge(x0,x1,x2,y0,y1,y2): #3点が同一直線かどうか
    return (y0-y1)*(x2-x1) == (x0-x1)*(y2-y1)

n,k = map(int,input().split())
XY = [tuple(map(int,input().split())) for _ in range(n)]
if k <= 1:
    ans = "Infinity"
else:
    Ans = [0] * (n+1)
    for a in range(n):
        for b in range(n):
            if b == a:
                continue
            cnt = 0
            for c in range(n):
                if judge(XY[a][0],XY[b][0],XY[c][0],XY[a][1],XY[b][1],XY[c][1]):
                    cnt += 1
            Ans[cnt] += 1
    for i in range(2,n+1):
        Ans[i] //= (i*(i-1))
    ans = 0
    for i in range(k,n+1):
        ans += Ans[i]
print(ans)