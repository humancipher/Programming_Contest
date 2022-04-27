def solve(T,n):
    ts = sum(T)
    dp = [[False for _ in range(ts+1)] for _ in range(n+1)]
    #dp[i][j]:i番目までで和jを作れるか
    for i in range(n):
        dp[i][0] = True
    
    for i in range(1,n+1):
        for j in range(1,ts+1):
            if j - T[i-1] >= 0:
                if dp[i-1][j-T[i-1]]:
                    dp[i][j] = True
            if dp[i-1][j]:
                dp[i][j] = True
    mid = (ts+1)//2
    for j in range(mid,ts+1):
        if dp[n][j]:
            return j

def main():
    n = int(input())
    T = list(map(int,input().split()))
    print(solve(T,n))

if __name__ == "__main__":
    main()
