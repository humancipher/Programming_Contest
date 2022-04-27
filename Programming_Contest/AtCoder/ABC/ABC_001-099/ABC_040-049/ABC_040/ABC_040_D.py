class UF:
    def __init__(self,n):
        self.P = [i for i in range(n)]
        self.S = [1] * n #グループiの同族数（rootだけ正しい）
        self.n = n
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
                self.S[self.root(y)] += self.S[self.root(x)]
                self.P[self.root(x)] = self.root(y)
            else:
                self.S[self.root(x)] += self.S[self.root(y)]
                self.P[self.root(y)] = self.root(x)
    def getS(self,x):
        return self.S[self.root(x)]

def main():
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    G = []
    for _ in range(m):
        a,b,y = map(int,input().split())
        G.append((a-1,b-1,y))
    G.sort(key = lambda x:x[2],reverse=True)
    q = int(input())
    Ans = [1] * q
    H = []
    for i in range(q):
        v,w = map(int,input().split())
        H.append((i,v-1,w))
    H.sort(key = lambda x:x[2],reverse=True)
    uf = UF(n)
    pg,ph = 0,0
    while pg < m and ph < q:
        while G[pg][2] > H[ph][2]:
            a,b,y = G[pg]
            uf.unite(a,b)
            if pg < m-1:
                pg += 1
            else:
                break
        i,v,w = H[ph]
        Ans[i] = uf.getS(v)
        ph += 1
    for i in range(q):
        print(Ans[i])

if __name__ == "__main__":
    main()
