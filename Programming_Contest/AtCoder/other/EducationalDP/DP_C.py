def solve(N,A):
    dp = [[0] * 3 for _ in range(N)]
    for j in range(3):
        dp[0][j] = A[0][j]
    for i in range(1,N):
        for j in range(3):
            dp[i][j] = max(dp[i-1][(j+1)%3]+A[i][j],dp[i-1][(j+2)%3]+A[i][j])
    ans = 0
    for j in range(3):
        ans = max(ans,dp[N-1][j])
    return ans

def main():
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]
    print(solve(N,A))

if __name__ == "__main__":
    main()
