class UnionFind:
    def __init__(self,n):
        self.L = [i for i in range(n+1)]
    def depth(self,a):
        cnt = 0
        while self.L[a] != a:
            a = self.L[a]
            cnt += 1
        return cnt
    def root(self,a):
        while self.L[a] != a:
            a = self.L[a]
        return a
    def same(self,a,b):
        return self.root(a) == self.root(b)
    def union(self,a,b):
        if self.depth(a) < self.depth(b):
            self.L[self.root(a)] = self.root(b)
        else:
            self.L[self.root(b)] = self.root(a)

def solve(A,n):
    uf = UnionFind(2*10**5)
    for i in range(n//2):
        if A[i] != A[n-1-i]:
            uf.union(A[i],A[n-1-i])
    ans = 0
    for i in range(1,2*10**5+1):
        if uf.depth(i) != 0:
            ans += 1
    return ans

def main():
    n = int(input())
    A = list(map(int,input().split()))
    print(solve(A,n))

if __name__ == "__main__":
    main()
