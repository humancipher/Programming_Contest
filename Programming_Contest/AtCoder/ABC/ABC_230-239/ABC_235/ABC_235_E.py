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
    n,m,q = map(int,input().split())
    G = list() #[重み,from,to,元々のedgeかどうか]
    Ans = [None] * q
    for _ in range(m):
        a,b,c = map(int,input().split())
        G.append([a-1,b-1,c,0,-1])
    for i in range(q):
        u,v,w = map(int,input().split())
        G.append([u-1,v-1,w,1,i])
    G.sort(key = lambda x:x[2])
    uf = UF(n)
    for i in range(m+q):
        a,b,c,d,e = G[i][0],G[i][1],G[i][2],G[i][3],G[i][4]
        if d == 0: #元々あるedgeの場合
            uf.unite(a,b)
        else: #queryで追加するedgeの場合
            if uf.same(a,b):
                Ans[e] = "No"
            else:
                Ans[e] = "Yes"
    for i in range(q):
        print(Ans[i])

if __name__ == "__main__":
    main()
