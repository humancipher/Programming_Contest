a,b = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [[0] * (b+1) for _ in range(a+1)]
#dp[i][j]:(i,j)から始めた場合の先手のスコア-後手のスコア
for i in reversed(range(a)):
    if (i+b) % 2 == 0:
        dp[i][b] = dp[i+1][b] + A[i]
    else:
        dp[i][b] = dp[i+1][b] - A[i]
for j in reversed(range(b)):
    if (a+j) % 2 == 0:
        dp[a][j] = dp[a][j+1] + B[j]
    else:
        dp[a][j] = dp[a][j+1] - B[j]

for i in reversed(range(a)):
    for j in reversed(range(b)):
        if (i+j) % 2 == 0:
            dp[i][j] = max(dp[i+1][j] + A[i],dp[i][j+1] + B[j])
        else:
            dp[i][j] = min(dp[i+1][j] - A[i],dp[i][j+1] - B[j])

sumAB = sum(A) + sum(B)
if (sumAB) % 2 == 0:
    ans = sumAB//2 + dp[0][0]//2
else:
    ans = sumAB//2 + (dp[0][0]+1)//2
print(ans)