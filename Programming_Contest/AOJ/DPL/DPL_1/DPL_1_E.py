def ED(s1,s2):
    m,n = len(s1),len(s2)
    """
    方針：DP
    s1,s2のどちらかが空白文字列ならもう一方の長さ
    s1のi文字目,s2のj文字目まで読み,
    最後が一致していたらその直前までの操作で十分
    一致していなかったら3種の操作のどれかを行う
    """
    dp = [[None for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

    return dp[m][n]

def main():
    s1 = input()
    s2 = input()

    ans = ED(s1,s2)
    print(ans)

if __name__ == "__main__":
    main()
