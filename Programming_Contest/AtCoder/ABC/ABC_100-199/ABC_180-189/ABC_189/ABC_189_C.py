N = int(input())
A = list(map(int,input().split()))

ans = 0
for l in range(N):
    x = A[l]
    tmp = 0
    for r in range(l,N):
        x = min(x,A[r])
        tmp = max(tmp,x * (r-l+1))
    ans = max(ans,tmp)

print(ans)
