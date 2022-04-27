N,M = map(int,input().split())
A = set([int(input()) for _ in range(M)])
Div = 10**9+7
#dp[i]:i段目にたどり着く移動方法のパターン数
dp = [0 for _ in range(N+1)]
dp[0] = 1
if 1 not in A:
    dp[1] = 1

for i in range(2,N+1):
    if i not in A:
        dp[i] = (dp[i-1] + dp[i-2]) % Div

print(dp[N])
