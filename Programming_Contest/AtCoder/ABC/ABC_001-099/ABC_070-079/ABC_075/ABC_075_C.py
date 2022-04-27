class UnionFind:
    def __init__(self,N):
        self.P = [i for i in range(N+1)]
        self.N = N
    
    def root(self,a):
        while self.P[a] != a:
            a = self.P[a]
        return a
    
    def same(self,a,b):
        return self.root(a) == self.root(b)
    
    def depth(self,a):
        h = 0
        while self.P[a] != a:
            a = self.P[a]
            h += 1
        return h
    
    def union(self,a,b):
        if not self.same(a,b):
            if self.depth(a) < self.depth(b):
                self.P[self.root(a)] = self.root(b)
            else:
                self.P[self.root(b)] = self.root(a)

    def groupcount(self):
        S = set()
        for i in range(1,self.N + 1):
            S.add(self.root(self.P[i]))
        return len(S)

def judge(E,N,M):
    uf = UnionFind(N)
    for a,b in E:
        uf.union(a,b)
    return uf.groupcount() > 1

def solve(E,N,M):
    ans = 0
    for i in range(M):
        E_set = set(E[:i] + E[i+1:])
        if judge(E_set,N,M):
            ans += 1
    return ans

def main():
    N,M = map(int,input().split())
    E = [tuple(map(int,input().split())) for _ in range(M)]
    print(solve(E,N,M))

if __name__ == "__main__":
    main()

