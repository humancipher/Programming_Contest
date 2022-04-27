def DP(A,N,S,M):
    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = 1
    #dp[i][j]:要素数i個以下,i番目までで和がjである部分集合の個数
    for i in range(1,N+1):
        for j in range(S+1):
            dp[i][j] = 2 * dp[i-1][j]
            dp[i][j] %= M
            if j - A[i-1] >= 0:
                dp[i][j] += dp[i-1][j-A[i-1]]
                dp[i][j] %= M

    return dp[N][S]

def main():
    N,S = map(int,input().split())
    A = list(map(int,input().split()))
    M = 998244353

    ans = DP(A,N,S,M)
    print(ans)

if __name__ == "__main__":
    main()
