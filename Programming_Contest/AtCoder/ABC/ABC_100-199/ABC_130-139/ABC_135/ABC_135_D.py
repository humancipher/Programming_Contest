mod = 10**9+7

def solve(S,N):
    S = "".join([S[N-i-1] for i in range(N)])
    dp = [[0] * 13 for _ in range(N+1)] #dp[i][j]:下からi桁目まで見て13で割った余りがjになるパターン数
    dp[0][0] = 1
    digit = 1
    for i in range(1,N+1):
        if S[i-1] != "?":
            for j in range(13):
                dp[i][(j+digit*int(S[i-1]))%13] += dp[i-1][j]
                dp[i][(j+digit*int(S[i-1]))%13] %= mod
        else:
            for k in range(10): #?の値で場合分け
                for j in range(13):
                    dp[i][(j+digit*k)%13] += dp[i-1][j]
                    dp[i][(j+digit*k)%13] %= mod
        digit *= 10
        digit %= 13
    return dp[N][5]

def main():
    S = input()
    print(solve(S,len(S)))

if __name__ == "__main__":
    main()
