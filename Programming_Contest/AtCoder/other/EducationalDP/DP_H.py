mod = 10**9+7

def solve(A,h,w):
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for i in range(1,h):
        if A[i][0] == ".":
            dp[i][0] += dp[i-1][0]
    for j in range(1,w):
        if A[0][j] == ".":
            dp[0][j] += dp[0][j-1]
    for i in range(1,h):
        for j in range(1,w):
            if A[i][j] == ".":
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                dp[i][j] %= mod
    return dp[h-1][w-1]

def main():
    h,w = map(int,input().split())
    A = [input() for _ in range(h)]
    print(solve(A,h,w))

if __name__ == "__main__":
    main()
