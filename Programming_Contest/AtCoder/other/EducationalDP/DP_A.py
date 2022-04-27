INF = 10**10

def solve(H,N):
    dp = [INF for _ in range(N)] #dp[i]:足場iまでの最小コスト
    dp[0] = 0
    dp[1] = abs(H[1]-H[0])
    for i in range(2,N):
        dp[i] = min(dp[i],dp[i-1]+abs(H[i]-H[i-1]),dp[i-2]+abs(H[i]-H[i-2]))
    return dp[N-1]

def main():
    N = int(input())
    H = list(map(int,input().split()))
    print(solve(H,N))

if __name__ == "__main__":
    main()
