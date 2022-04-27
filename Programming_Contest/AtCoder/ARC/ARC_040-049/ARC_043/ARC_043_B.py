def main():
    from bisect import bisect_right
    from itertools import accumulate
    import sys
    mod = 10**9+7
    input = sys.stdin.readline
    n = int(input())
    D = [int(input()) for _ in range(n)]
    D.sort()
    dp = [1] * n #dp[i]:A[i]を最後に使うパターン
    for _ in range(3):
        dp = list(accumulate(dp))
        ndp = [0] * n
        for i in range(n):
            bs = bisect_right(D,D[i]//2)
            if bs > 0:
                ndp[i] += dp[bs-1]
                ndp[i] %= mod
        dp = ndp
    print(sum(dp) % mod)

if __name__ == "__main__":
    main()
