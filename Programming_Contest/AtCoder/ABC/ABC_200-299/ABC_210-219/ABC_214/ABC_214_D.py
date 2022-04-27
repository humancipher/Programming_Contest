from heapq import heapify,heappop,heappush

class UF:
    def __init__(self,n):
        self.P = [i for i in range(n+1)]
        self.S = [1] * (n+1)
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
    def union(self,x,y):
        if not self.same(x,y):
            if self.depth(x) < self.depth(y):
                self.S[self.root(y)] += self.S[self.root(x)]
                self.P[self.root(x)] = self.P[self.root(y)]
            else:
                self.S[self.root(x)] += self.S[self.root(y)]
                self.P[self.root(y)] = self.P[self.root(x)]
    def getS(self,x):
        return self.S[x]

def main():
    n = int(input())
    HQ = []
    heapify(HQ)
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        heappush(HQ,[w,u,v])
    uf = UF(n)
    ans = 0
    for _ in range(n-1):
        [w,u,v] = heappop(HQ)
        ans += w * uf.getS(uf.root(u)) * uf.getS(uf.root(v))
        uf.union(u,v)
    print(ans)

if __name__ == "__main__":
    main()
