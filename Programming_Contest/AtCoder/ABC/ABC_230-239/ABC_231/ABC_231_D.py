class UF:
    def __init__(self,n):
        self.P = [i for i in range(n)]
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
        return self.root(x) == self.root(y)
    def unite(self,x,y):
        if not self.same(x,y):
            if self.depth(x) < self.depth(y):
                self.P[self.root(x)] = self.root(y)
            else:
                self.P[self.root(y)] = self.root(x)

def main():
    n,m = map(int,input().split())
    AB = []
    G = [list() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        AB.append([a-1,b-1])
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = "Yes"
    for i in range(n):
        if len(G[i]) > 2:
            ans = "No"
            break
    if ans == "Yes":
        uf = UF(n)
        for a,b in AB:
            if not uf.same(a,b):
                uf.unite(a,b)
            else:
                ans = "No"
                break
    print(ans)

if __name__ == "__main__":
    main()
