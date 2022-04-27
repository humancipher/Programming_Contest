def solve(WV,N,W):
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        w,v = WV[i][0],WV[i][1]
        for j in range(W+1):
            if j >= w:
                dp[i+1][j] = max(dp[i][j],dp[i][j-w]+v)
            else:
                dp[i+1][j] = dp[i][j]
    return dp[N][W]

def main():
    N,W = map(int,input().split())
    WV = [list(map(int,input().split())) for _ in range(N)]
    print(solve(WV,N,W))

if __name__ == "__main__":
    main()
