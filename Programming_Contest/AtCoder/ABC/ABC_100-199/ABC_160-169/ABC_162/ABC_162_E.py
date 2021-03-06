def sumGCD(N,K,M):
    dp = [None for _ in range(K+1)]
    #dp[i]:gcd(A) % i == 0を満たすAの個数
    for i in reversed(range(1,K+1)):
        dp[i] = pow(K//i,N,M)
        for j in range(2,K//i+1):
            dp[i] -= dp[i*j]
            dp[i] %= M

    output = 0
    for i in range(1,K+1):
        output += (dp[i]*i)
        output %= M

    return output

def main():
    N,K = map(int,input().split())

    print(sumGCD(N,K,10**9+7))

if __name__ == "__main__":
    main()
