def solve(P,n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)] #dp[i][j]:i枚投げてj枚表の確率
    dp[0][0] = 1
    for i in range(1,n+1):
        dp[i][0] = (1-P[i-1]) * dp[i-1][0]
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i][j] = P[i-1] * dp[i-1][j-1] + (1-P[i-1]) * dp[i-1][j]
    ans = 0
    for j in range(n//2+1,n+1):
        ans += dp[n][j]
    return ans

def main():
    n = int(input())
    P = list(map(float,input().split()))
    print(solve(P,n))

if __name__ == "__main__":
    main()
