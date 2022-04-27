n = int(input())
S = input()
ans = n
for i in range(n):
    L = S[:i]
    R = S[i:]
    dp = [[0] * (len(R)+1) for _ in range(len(L)+1)]
    #L,Rの最長共通部分列の長さを求めたい
    for a in range(len(L)):
        for b in range(len(R)):
            if L[a] == R[b]:
                dp[a+1][b+1] = max(dp[a+1][b+1],dp[a][b] + 2,dp[a+1][b],dp[a][b+1])
                ans = min(ans,n-dp[a+1][b+1])
            else:
                dp[a+1][b+1] = max(dp[a+1][b+1],dp[a+1][b],dp[a][b+1])
                ans = min(ans,n-dp[a+1][b+1])
print(ans)