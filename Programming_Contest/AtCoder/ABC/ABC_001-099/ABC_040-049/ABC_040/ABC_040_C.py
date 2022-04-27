def move(a,N):
    dp = [None for _ in range(N)]
    dp[0],dp[1] = 0,abs(a[1]-a[0])

    for i in range(2,N):
        dp[i] = min(dp[i-1]+abs(a[i]-a[i-1]),dp[i-2]+abs(a[i]-a[i-2]))

    return dp[N-1]

def main():
    N = int(input())
    a = list(map(int,input().split()))

    ans = move(a,N)
    print(ans)

if __name__ == "__main__":
    main()
