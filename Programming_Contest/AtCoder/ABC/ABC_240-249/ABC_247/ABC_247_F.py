mod = 998244353

class UF:
    def __init__(self,n):
        self.P = [i for i in range(n+1)]
        self.S = [1] * (n+1)
    def root(self,x):
        while x != self.P[x]:
            x = self.P[x]
        return x
    def depth(self,x):
        cnt = 0
        while x != self.P[x]:
            x = self.P[x]
            cnt += 1
        return cnt
    def same(self,x,y):
        return self.root(x) == self.root(y)
    def unite(self,x,y):
        if not self.same(x,y):
            if self.depth(x) < self.depth(y):
                self.S[self.root(y)] += self.S[self.root(x)]
                self.P[self.root(x)] = self.root(y)
            else:
                self.S[self.root(x)] += self.S[self.root(y)]
                self.P[self.root(y)] = self.root(x)

def main():
    n = int(input())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))

    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 3
    for i in range(3,n+2):
        dp[i] = (dp[i-1]+dp[i-2]) % mod
    uf = UF(n)
    for i in range(n):
        uf.unite(P[i],Q[i])
    ans = 1
    for i in range(1,n+1):
        if i == uf.root(i):
            ans *= dp[uf.S[uf.root(i)]]
            ans %= mod
    print(ans)

if __name__ == "__main__":
    main()
