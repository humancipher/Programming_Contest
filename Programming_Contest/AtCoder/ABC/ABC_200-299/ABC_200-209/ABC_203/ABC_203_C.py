n,k = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(n)]

AB.sort(key = lambda x:x[0])

ans,prev = 0,0
for a,b in AB:
    if k >= a - prev:
        k += (b - (a - prev))
        ans = a
        prev = a
    else:
        ans += k
        k = 0
        break
if k != 0:
    ans += k
print(ans)
