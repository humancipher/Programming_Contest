class UF():
    def __init__(self,N):
        self.N = N
        self.P = [-i for i in range(N+1)]
    
    def root(self,a):
        while a > 0:
            a = self.P[a]
        return a
    
    def depth(self,a):
        cnt = 0
        while a > 0:
            a = self.P[a]
            cnt += 1
        return cnt

    def same(self,a,b):
        return(self.root(a) == self.root(b))
    
    def union(self,a,b):
        if not self.same(a,b):
            if self.depth(a) >= self.depth(b):
                self.P[-self.root(b)] = -self.root(a)
            else:
                self.P[-self.root(a)] = -self.root(b)
    
    def solve(self):
        G = dict()
        ans = 0
        for i in range(1,self.N+1):
            g = self.root(self.P[i])
            if g not in G:
                G[g] = 1
            else:
                G[g] += 1
            ans = max(ans,G[g])
        return ans
    
def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    uf = UF(N)
    for a,b in AB:
        uf.union(a,b)
    
    print(uf.solve())

if __name__ == "__main__":
    main()
