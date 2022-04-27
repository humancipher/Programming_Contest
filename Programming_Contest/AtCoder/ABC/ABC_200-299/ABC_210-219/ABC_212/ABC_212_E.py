def main():
    n,m,k = map(int,input().split())
    NG = set()
    for _ in range(m):
        u,v = map(int,input().split())
        NG.add((u,v))
    print(solve(NG,n,k))

def solve(NG,n,k):
    mod = 998244353
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    #dp[i][j]:i日目に街jに来るパターン数
    dp[0][1] = 1
    for i in range(1,k+1):
        dp_sum = 0
        for j in range(1,n+1):
            dp_sum += dp[i-1][j]
            dp_sum %= mod
        for j in range(1,n+1):
            dp[i][j] += (dp_sum - dp[i-1][j])
            dp[i][j] %= mod
        for (ga,gb) in NG:
            dp[i][ga] -= dp[i-1][gb]
            dp[i][ga] %= mod
            dp[i][gb] -= dp[i-1][ga]
            dp[i][gb] %= mod
    return dp[k][1]

if __name__ == "__main__":
    main()
