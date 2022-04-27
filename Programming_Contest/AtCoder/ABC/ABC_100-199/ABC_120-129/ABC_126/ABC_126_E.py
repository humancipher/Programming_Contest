class UF:
    def __init__(self,N):
        self.P = [i for i in range(N+1)]
        self.N = N
    def root(self,a):
        while self.P[a] != a:
            a = self.P[a]
        return a
    def depth(self,a):
        cnt = 0
        while self.P[a] != a:
            a = self.P[a]
            cnt += 1
        return cnt
    def same(self,a,b):
        return self.root(a) == self.root(b)
    def union(self,a,b):
        if not self.same(a,b):
            if self.depth(a) < self.depth(b):
                self.P[self.root(a)] = self.P[self.root(b)]
            else:
                self.P[self.root(b)] = self.P[self.root(a)]
    def kind_cnt(self):
        K = set()
        for i in range(1,self.N+1):
            K.add(self.root(self.P[i]))
        return len(K)

def solve(XY,N):
    uf = UF(N)
    for x,y in XY:
        uf.union(x,y)
    return uf.kind_cnt()

def main():
    N,M = map(int,input().split())
    XY = [list(map(int,input().split())) for _ in range(M)] #実はZはいらない
    for i in range(M):
        XY[i].pop()
    print(solve(XY,N))

if __name__ == "__main__":
    main()
