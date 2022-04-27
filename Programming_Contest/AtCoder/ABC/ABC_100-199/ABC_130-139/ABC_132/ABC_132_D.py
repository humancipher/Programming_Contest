#pypyなら間に合う

def DP(N,M):
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for j in range(N+1):
        dp_sum[0][j] = 1
    #dp[i][j]:i個の項で和がj
    #dp_sum[i][j]:dp[i][0]+...+dp[i][j]
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j] = (dp_sum[i-1][j-1] - dp_sum[i-1][i-1] + dp[i-1][i-1]) % M
            dp_sum[i][j] = (dp_sum[i][j-1] + dp[i][j]) % M

    return dp

def main():
    N,K = map(int,input().split())
    M = 10**9+7

    dp = DP(N,M)

    comb = 1
    for i in range(1,K+1):
        comb *= (N - K + 2 - i)
        comb *= pow(i,M-2,M)
        comb %= M
        if i > N - K + 1:
            comb = 0
        print((comb * dp[i][K]) % M)

if __name__ == "__main__":
    main()
