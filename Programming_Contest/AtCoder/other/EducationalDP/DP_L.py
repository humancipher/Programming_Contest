n = int(input())
A = list(map(int,input().split()))

if n == 1:
    print(A[0])
else:
    dp = [[None] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = A[i]

    for diff in range(1,n):
        dp[0][diff] = A[0] - dp[1][diff]
        if dp[n-1-diff][n-1] != None:
            dp[n-1-diff][n-1] = max(A[n-1] - dp[n-diff][n-2],dp[n-1-diff][n-1])
        else:
            dp[n-1-diff][n-1] = A[n-1] - dp[n-1-diff][n-2]
        for i in range(n-diff):
            pat1 = A[i] - dp[i+1][i+diff]
            pat2 = A[i+diff] - dp[i][i+diff-1]
            dp[i][i+diff] = max(pat1,pat2)
    print(dp[0][n-1])
