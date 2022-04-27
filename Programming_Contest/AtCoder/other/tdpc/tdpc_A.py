n = int(input())
P = list(map(int,input().split()))

dp = [0] * (sum(P)+1)
dp[0] = 1
for i in range(n):
    p = P[i]
    for j in reversed(range(len(dp))):
        if j-p >= 0:
            if dp[j] == 0 and dp[j-p] ==1:
                dp[j] = 1

print(sum(dp))
