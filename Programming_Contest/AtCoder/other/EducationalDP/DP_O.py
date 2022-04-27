mod = 10**9+7

def hw(x):
    cnt = 0
    while x > 0:
        if x % 2 == 1:
            cnt += 1
        x //= 2
    return cnt

def main():
    n = int(input())
    A = [list(map(int,input().split())) for _ in range(n)]
    
    HW = [[] for _ in range(n+1)]
    for i in range(2**n):
        HW[hw(i)].append(i)
    dp = [0] * (2**n) #dp[i][j]:i人目の男まででマッチングした女のパターンがjであるパターン数
    dp[0] = 1
    for i in range(n):
        ndp = [0] * (2**n)
        for now in HW[i]:
            for j in range(n):
                if now & 2**j == 0 and A[i][j] == 1:
                    ndp[now | 2**j] += dp[now]
                    ndp[now | 2**j] %= mod
        dp = ndp
    print(dp[2**n-1])

if __name__ == "__main__":
    main()
