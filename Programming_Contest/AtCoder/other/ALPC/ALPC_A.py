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
    n,q = map(int,input().split())
    uf = UF(n)
    Ans = list()
    for _ in range(q):
        t,u,v = map(int,input().split())
        if t == 0:
            uf.unite(u-1,v-1)
        else:
            if uf.same(u-1,v-1):
                Ans.append(1)
            else:
                Ans.append(0)
    for i in range(len(Ans)):
        print(Ans[i])

if __name__ == "__main__":
    main()