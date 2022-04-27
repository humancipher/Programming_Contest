from bisect import bisect_left
INF = 10**6

def main():
    n = int(input())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    Qrev = [None] * (n+1)
    for i in range(n):
        Qrev[Q[i]] = i
    ans = 0
    A = [[] for _ in range(n)]
    for i in range(n):
        for j in range(1,n // P[i] + 1):
            A[i].append(Qrev[P[i]*j])
        A[i].sort(reverse=True)

    dp = [INF] * n #dp[i]:長さiを達成する末尾の最小値
    for i in range(n):
        for j in range(len(A[i])):
            bs = bisect_left(dp,A[i][j])
            dp[bs] = A[i][j]
        
    ans = 1
    for i in range(n):
        if dp[i] != INF:
            ans = i+1
        else:
            break
    print(ans)

if __name__ == "__main__":
    main()
