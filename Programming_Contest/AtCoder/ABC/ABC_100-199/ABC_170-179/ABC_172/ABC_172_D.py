from math import sqrt

def solve(N):
    dp = [2 for _ in range(N+1)]
    dp[1] = 1

    for i in range(2,int(sqrt(N)) + 1):
        for j in range(2, N//i + 1):
            if j <= int(sqrt(N)):
                dp[i * j] += 1
            else:
                dp[i * j] += 2

    ans = 0
    for i in range(1,N+1):
        ans += (i * dp[i])

    return ans

def main():
    N = int(input())

    print(solve(N))

if __name__ == "__main__":
    main()
