a,b = map(int,input().split())
ans = 1
for s in range(1,b+1):
    x0 = b // s
    if (x0-1)*s >= a:
        ans = s
print(ans)
