from bisect import bisect_left

INF = 10**5

n = int(input())
C = [int(input()) for _ in range(n)]

dp = [INF] * (n+1)
#dp[i]:長さiの最長共通部分増加列の末尾の最小値
#注:このdpは(INFの部分以外)常に単調増加になるので二分探索が使える

for i in range(n):
    pt = bisect_left(dp,C[i])
    dp[pt] = C[i]

ans = n - bisect_left(dp,INF)
print(ans)
