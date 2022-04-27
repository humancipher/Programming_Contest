from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    S = list(input().rstrip())
    X = list(input().rstrip())
    for i in range(n):
        S[i] = int(S[i])
    #dp[i][j]:i手目で余りがjのときに高橋君が勝つかどうか
    dp = [False] * 7
    dp[0] = True
    for i in reversed(range(n)):
        ndp = [False] * 7
        for j in range(7):
            r1 = 10*j % 7
            r2 = (10*j+S[i]) % 7
            if X[i] == "T":
                if dp[r1] | dp[r2]:
                    ndp[j] = True
            else:
                if dp[r1] & dp[r2]:
                    ndp[j] = True
        dp = ndp

    if dp[0]:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == "__main__":
    main()
