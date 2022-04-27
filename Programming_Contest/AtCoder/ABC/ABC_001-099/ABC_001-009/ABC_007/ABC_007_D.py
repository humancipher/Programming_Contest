def solve(n):
    n = str(n)
    dp = [[[0] * 2 for _ in range(2)] for _ in range(len(n)+1)]
    #dp[i+1][0][0]:左からi桁目がn未満の禁止数のパターン数
    #dp[i+1][1][0]:左からi桁目がnと一致の禁止数のパターン数
    #dp[i+1][0][1]:左からi桁目がn未満の非禁止数のパターン数
    #dp[i+1][1][1]:左からi桁目がnと一致の非禁止数のパターン数
    dp[0][1][1] = 1
    for i in range(len(n)):
        ns = int(n[i])
        for x in range(10):
            if x == 4 or x == 9:
                dp[i+1][0][0] += dp[i][0][1]
                dp[i+1][0][0] += dp[i][0][0]
            else:
                dp[i+1][0][0] += dp[i][0][0]
                dp[i+1][0][1] += dp[i][0][1]
        for x in range(ns):
            if x == 4 or x == 9:
                dp[i+1][0][0] += dp[i][1][1]
                dp[i+1][0][0] += dp[i][1][0]
            else:
                dp[i+1][0][0] += dp[i][1][0]
                dp[i+1][0][1] += dp[i][1][1]
        if ns == 4 or ns == 9:
            dp[i+1][1][0] += dp[i][1][1]
            dp[i+1][1][0] += dp[i][1][0]
        else:
            dp[i+1][1][0] += dp[i][1][0]
            dp[i+1][1][1] += dp[i][1][1]
    return dp[-1][0][0]+dp[-1][1][0]

def main():
    a,b = map(int,input().split())
    ans = solve(b)-solve(a-1)
    print(ans)

if __name__ == "__main__":
    main()
