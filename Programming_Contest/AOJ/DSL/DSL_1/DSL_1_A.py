class UF:
    def __init__(self,n):
        self.P = [i for i in range(n)]
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
        if not self.same(x,y):
            if self.depth(x) < self.depth(y):
                self.P[self.root(x)] = self.root(y)
            else:
                self.P[self.root(y)] = self.root(x)

n,q = map(int,input().split())
uf = UF(n)
for _ in range(q):
    com,x,y = map(int,input().split())
    if com == 0:
        uf.union(x,y)
    else:
        if uf.same(x,y):
            print(1)
        else:
            print(0)
