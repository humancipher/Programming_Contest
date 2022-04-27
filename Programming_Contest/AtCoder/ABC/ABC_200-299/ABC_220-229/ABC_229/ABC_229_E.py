class UF:
    def __init__(self,n):
        self.P = [i for i in range(n)]
        self.S = [1] * (n)
    def depth(self,x):
        cnt = 0
        while self.P[x] != x:
            x = self.P[x]
            cnt += 1
        return cnt
    def root(self,x):
        while self.P[x] != x:
            x = self.P[x]
        return x
    def same(self,x,y):
        return self.root(self.P[x]) == self.root(self.P[y])
    def unite(self,x,y):
        if not self.same(x,y):
            if self.depth(x) < self.depth(y):
                self.S[self.root(y)] += self.S[self.root(x)]
                self.P[self.root(x)] = self.P[self.root(y)]
            else:
                self.S[self.root(x)] += self.S[self.root(y)]
                self.P[self.root(y)] = self.P[self.root(x)]
    def getS(self,x):
        return self.S[self.root(x)]

def main():
    n,m = map(int,input().split())
    G = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)
    Ans,tmp = [0],0
    uf = UF(n)
    for i in reversed(range(1,n)):
        Roots = set()
        for nxt in G[i]:
            if nxt > i:
                Roots.add(uf.root(nxt))
                uf.unite(i,nxt)
        Roots.discard(i)
        tmp += 1 - len(Roots)
        Ans.append(tmp)
    for i in reversed(range(n)):
        print(Ans[i])

if __name__ == "__main__":
    main()
