class UnionFind:
    def __init__(self,N):
        self.N = N
        self.P = [i for i in range(N+1)]
    def root(self,a):
        while a != self.P[a]:
            a = self.P[a]
        return a
    def depth(self,a):
        cnt = 0
        while a != self.P[a]:
            a = self.P[a]
            cnt += 1
        return cnt
    def same(self,a,b):
        return self.root(a) == self.root(b)
    def union(self,a,b):
        if self.depth(a) >= self.depth(b):
            self.P[self.root(b)] = self.root(a)
        else:
            self.P[self.root(a)] = self.root(b)
    def group(self):
        GR = [[] for _ in range(self.N+1)]
        for i in range(1,self.N+1):
            GR[self.root(i)].append(i)
        return GR

def solve(G,A,B,N):
    uf = UnionFind(N)
    for c,d in G:
        uf.union(c,d)
    GR = uf.group()
    ans = "Yes"
    for i in range(1,N+1):
        a,b = 0,0
        for g in GR[i]:
            a += A[g-1]
            b += B[g-1]
        if a != b:
            ans = "No"
            break
    return ans

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    G = [list(map(int,input().split())) for _ in range(M)]
    print(solve(G,A,B,N))

if __name__ == "__main__":
    main()
