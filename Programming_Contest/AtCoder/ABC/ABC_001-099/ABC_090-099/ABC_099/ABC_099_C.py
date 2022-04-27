def solve(n):
    M = [1]
    n6,n9 = 6,9
    while n6 <= n:
        M.append(n6)
        n6 *= 6
    while n9 <= n:
        M.append(n9)
        n9 *= 9
    dp = [n for _ in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1):
        for m in M:
            if i-m >= 0:
                dp[i] = min(dp[i],dp[i-m]+1)
    return dp[n]

n = int(input())
print(solve(n))
