def solve(s,t):
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    
    x,y = len(s)-1,len(t)-1
    le = dp[-1][-1]
    Ans = []
    while le > 0:
        if s[x] == t[y]:
            Ans.append(s[x])
            x -= 1
            y -= 1
            le -= 1
        else:
            if dp[x][y+1] >= dp[x+1][y]:
                x -= 1
            else:
                y -= 1
    for i in range(len(Ans) // 2):
        Ans[i],Ans[-1-i] = Ans[-1-i],Ans[i]
    return "".join(Ans)

s = input()
t = input()
print(solve(s,t))

