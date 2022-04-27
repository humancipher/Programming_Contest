def solve(N):
    M = 10**9+7
    DP = [0 for _ in range(N+1)]
    DP[0] = 1
    for n in range(N+1):
        for i in range(3,n+1):
            DP[n] += DP[n-i]
            DP[n] %= M

    return DP[N]

def main():
    S = int(input())
    print(solve(S))

if __name__ == "__main__":
    main()
