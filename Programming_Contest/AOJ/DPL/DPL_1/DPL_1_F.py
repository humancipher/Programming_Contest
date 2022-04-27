def KP(Val,Wei,N,W):
    v_sum = sum(Val)
    #dp[i][j]:i番目までの品,価値の合計がjでの最小の重さ
    INF = 10**9+1
    dp = [[INF for _ in range(v_sum+1)] for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 0

    for i in range(N):
        for j in range(v_sum+1):
            if j - Val[i] >= 0:
                dp[i+1][j] = min(dp[i][j-Val[i]]+Wei[i],dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]

    output = 0
    for j in range(v_sum+1):
        if dp[N][j] <= W:
            output = j

    return output

def main():
    N,W = map(int,input().split())
    VW = [list(map(int,input().split())) for _ in range(N)]
    Val = [VW[i][0] for i in range(N)]
    Wei = [VW[i][1] for i in range(N)]
    ans = KP(Val,Wei,N,W)
    print(ans)

if __name__ == "__main__":
    main()
