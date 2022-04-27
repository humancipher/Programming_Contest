INF = 10**10

def solve(H,N,K):
    dp = [INF for _ in range(N)] #dp[i]:i番目までの最小コスト
    dp[0] = 0
    for i in range(N):
        for j in range(1,K+1):
            if i-j >= 0:
                dp[i] = min(dp[i],dp[i-j] + abs(H[i-j]-H[i]))
    return dp[N-1]

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    print(solve(H,N,K))

if __name__ == "__main__":
    main()
