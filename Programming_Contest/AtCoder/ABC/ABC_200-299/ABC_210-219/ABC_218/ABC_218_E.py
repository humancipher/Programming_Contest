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
    
    def union(self,x,y):
        if self.depth(x) < self.depth(y):
            self.P[self.root(x)] = self.root(y)
        else:
            self.P[self.root(y)] = self.root(x)

def solve(C,n,e_sum):
    uf = UF(n)
    cnt = 0
    tmp = -1 #Cから直前に取り出した辺のコスト
    while (cnt < n-1 or tmp < 0) and len(C) > 0:
        CL = C.pop()
        a,b,c = CL[0],CL[1],CL[2]
        if (not uf.same(a,b)) or c <= 0:
            if not uf.same(a,b):
                cnt += 1
                uf.union(a,b)
            e_sum -= c
    return e_sum

def main():
    n,m = map(int,input().split())
    C = []
    e_sum = 0
    for _ in range(m):
        a,b,c = map(int,input().split())
        C.append([a-1,b-1,c])
        e_sum += c
    C.sort(reverse = True,key = lambda x:x[2])
    ans = solve(C,n,e_sum)
    print(ans)

if __name__ == "__main__":
    main()
