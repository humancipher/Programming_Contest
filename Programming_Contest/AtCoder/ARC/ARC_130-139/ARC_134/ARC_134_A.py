n,l,w = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
pt = 0
for i in range(n):
    left = A[i]
    cnt = (left-pt)//w
    if (left-pt) % w != 0 and left >= pt:
        cnt += 1
    ans += max(0,cnt)
    pt = A[i]+w
cnt = (l-pt)//w
if (l-pt) % w != 0 and l >= pt:
    cnt += 1
ans += max(0,cnt)
print(ans)