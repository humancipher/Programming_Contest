mod = 10**9+7

class BIT:
    def __init__(self,n):
        self.Data = [0] * (n+1)
        self.n = n
    def plus(self,i,x):
        i += 1
        while i < self.n+1:
            self.Data[i] += x
            self.Data[i] %= mod
            i += i&(-i)
    def subque(self,i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.Data[i]
            ans %= mod
            i -= i&(-i)
        return ans
    def query(self,left,right):
        return (self.subque(right)-self.subque(left-1)) % mod

def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))

    dp = [0] * (k+1)
    dp[0] = 1
    for i in range(n):
        ndp = [0] * (k+1)
        bit = BIT(k+1)
        for j in range(k+1):
            bit.plus(j,dp[j])
        for j in range(k+1):
            tmp = bit.query(max(0,j-A[i]),j)
            ndp[j] = tmp
        dp = ndp
    print(dp[k])

if __name__ == "__main__":
    main()
