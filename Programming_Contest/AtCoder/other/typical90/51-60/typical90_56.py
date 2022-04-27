n,s = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(n)]

dp = [[False for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(s):
        if dp[i][j]:
            a,b = AB[i][0],AB[i][1]
            if j + a <= s:
                dp[i+1][j+a] = True
            if j + b <= s:
                dp[i+1][j+b] = True

if dp[n][s]:
    ans = ""
    pt = s
    for i in reversed(range(n)):
        a,b = AB[i][0],AB[i][1]
        flag = True
        if pt - a >= 0:
            if dp[i][pt-a]:
                pt -= a
                ans = "A" + ans
                flag = False
        if flag and pt - b >= 0:
            if dp[i][pt-b]:
                pt -= b
                ans = "B" + ans
    print(ans)
else:
    print("Impossible")
