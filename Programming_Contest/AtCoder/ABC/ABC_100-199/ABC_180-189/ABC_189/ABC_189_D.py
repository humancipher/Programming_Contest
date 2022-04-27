def solve(S,N):
    dp = [[0 for _ in range(2)] for _ in range(N+1)] #dp[i][j]:yi = jになる(x0,...,xi)のパターン数
    dp[0][0],dp[0][1] = 1,1
    for i in range(N):
        if S[i] == "AND":
            dp[i+1][0] = dp[i][0] * 2 + dp[i][1] * 1
            dp[i+1][1] = dp[i][0] * 0 + dp[i][1] * 1
        else:
            dp[i+1][0] = dp[i][0] * 1 + dp[i][1] * 0
            dp[i+1][1] = dp[i][0] * 1 + dp[i][1] * 2
    return dp[N][1]

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    print(solve(S,N))

if __name__ == "__main__":
    main()
