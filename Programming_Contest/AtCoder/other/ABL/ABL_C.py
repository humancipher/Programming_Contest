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
    def unite(self,x,y):
        if not self.same(x,y):
            if self.depth(x) < self.depth(y):
                self.P[self.root(x)] = self.root(y)
            else:
                self.P[self.root(y)] = self.root(x)

def main():
    n,m = map(int,input().split())
    uf = UF(n)
    for _ in range(m):
        a,b = map(int,input().split())
        uf.unite(a-1,b-1)
    Grp = set()
    for i in range(n):
        Grp.add(uf.root(i))
    print(len(Grp)-1)

if __name__ == "__main__":
    main()
