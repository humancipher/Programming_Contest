class UF:
    def __init__(self,n):
        self.P = [i for i in range(n+1)]
        self.E = [0] * (n+1) #E[i]:頂点iのグループの辺の数
        self.V = [1] * (n+1) #V[i]:頂点iのグループの頂点数
    def root(self,x):
        while self.P[x] != x:
            x = self.P[x]
        return x
    def depth(self,x):
        cnt = 0
        while self.P[x] != x:
            x = self.P[x]
            cnt += 1
        return cnt
    def same(self,x,y):
        return self.root(x) == self.root(y)
    def union(self,x,y):
        if self.root(x) == self.root(y):
            self.E[self.root(x)] += 1
        else:
            if self.depth(x) < self.depth(y):
                self.E[self.root(y)] += self.E[self.root(x)] + 1
                self.V[self.root(y)] += self.V[self.root(x)]
                self.P[self.root(x)] = self.root(y)
            else:
                self.E[self.root(x)] += self.E[self.root(y)] + 1
                self.V[self.root(x)] += self.V[self.root(y)]
                self.P[self.root(y)] = self.root(x)

def main():
    n,m = map(int,input().split())
    mod = 998244353
    uf = UF(n)
    for _ in range(m):
        u,v = map(int,input().split())
        uf.union(u,v)
    ans = 1
    for i in range(1,n+1):
        if uf.root(i) == i:
            if uf.V[i] >= 2 and uf.V[i] == uf.E[i]:
                ans *= 2
                ans %= mod
            else:
                ans = 0
    print(ans)

if __name__ == "__main__":
    main()
