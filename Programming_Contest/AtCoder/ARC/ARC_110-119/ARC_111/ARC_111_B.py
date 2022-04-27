class UF:
    def __init__(self,n,S):
        self.P = [i for i in range(n+1)]
        self.S = S
        self.isTree = [True] * (n+1)
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
        if self.same(x,y):
            self.isTree[self.root(x)] = False
            self.isTree[self.root(y)] = False
        else:
            if not (self.isTree[self.root(x)] and self.isTree[self.root(y)]):
                self.isTree[self.root(x)] = False
                self.isTree[self.root(y)] = False
            if self.depth(x) < self.depth(y):
                self.S[self.root(y)] += self.S[self.root(x)]
                self.P[self.root(x)] = self.root(y)
            else:
                self.S[self.root(x)] += self.S[self.root(y)]
                self.P[self.root(y)] = self.root(x)
    def getS(self,x):
        return self.S[x]
    def getisTree(self,x):
        return self.isTree[self.root(x)]

def main():
    n = int(input())
    S = [0] * (400001)
    AB = [list(map(int,input().split())) for _ in range(n)]
    for a,b in AB:
        if S[a] == 0:
            S[a] = 1
        if S[b] == 0:
            S[b] = 1

    uf = UF(400001,S)
    for a,b in AB:
        uf.union(a,b)
    ans = 0
    for i in range(1,400001):
        if S[i] != 0:
            if uf.depth(i) == 0: #グループ代表
                ans += uf.getS(i) - 1
                if not uf.getisTree(i):
                    ans += 1
    print(ans)

if __name__ == "__main__":
    main()
