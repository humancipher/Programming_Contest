n,k = map(int,input().split())
A = list(map(int,input().split()))

dp = [False for _ in range(k+1)] #dp[i]:iで先手になったら先手の勝利かどうか

for i in range(k+1):
    for a in A:
        if i - a >= 0:
            if not dp[i-a]:
                dp[i] = True
if dp[k]:
    print("First")
else:
    print("Second")
