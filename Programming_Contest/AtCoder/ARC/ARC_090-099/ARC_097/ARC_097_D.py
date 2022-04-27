class UF:
    def __init__(self,n):
        self.P = [i for i in range(n+1)]
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
    def unite(self,x,y):
        if not self.same(x,y):
            if self.depth(x) < self.depth(y):
                self.P[self.root(x)] = self.root(y)
            else:
                self.P[self.root(y)] = self.root(x)

n,m = map(int,input().split())
P = list(map(int,input().split()))
P = [0] + P
Inv = [None] * (n+1)
for i in range(n+1):
    Inv[P[i]] = i
uf = UF(n)
for _ in range(m):
    x,y = map(int,input().split())
    uf.unite(Inv[x],Inv[y])
ans = 0
for i in range(1,n+1):
    if uf.same(i,P[i]):
        ans += 1
print(ans)
