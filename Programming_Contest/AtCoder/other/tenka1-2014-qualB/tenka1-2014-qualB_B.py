def main():
    mod = 10**9+7
    import sys
    input = sys.stdin.readline
    n = int(input())
    S = input()
    T = [input().rstrip('\n') for _ in range(n)]
    dp = [0] * (len(S))
    dp[0] = 1
    for i in range(len(S)):
        for j in range(n):
            if i+len(T[j]) <= len(S):
                if S[i:i+len(T[j])] == T[j]:
                    dp[i+len(T[j])] += dp[i]
                    dp[i+len(T[j])] %= mod
    print(dp[len(S)-1])

if __name__ == "__main__":
    main()
