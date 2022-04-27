n,x = map(int,input().split())
dp = [False] * (10**4+1)
dp[0] = 1
for _ in range(n):
    ndp = [False] * (10**4+1)
    a,b = map(int,input().split())
    for i in range(10**4+1):
        if dp[i] and a+i <= 10**4:
            ndp[i+a] = True
        if dp[i] and b+i <= 10**4:
            ndp[i+b] = True
    dp = ndp
if dp[x]:
    print("Yes")
else:
    print("No")