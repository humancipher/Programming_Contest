class UF:
    def __init__(self,n):
        self.P = [i for i in range(n+1)]
        self.S = [1] * (n+1) #S[i]:グループiのサイズ(rootだけ正しければよい)
        self.break_sum = n*(n-1)
    
    def depth(self,x):
        cnt = 0
        while x != self.P[x]:
            x = self.P[x]
            cnt += 1
        return cnt
    
    def root(self,x):
        while x != self.P[x]:
            x = self.P[x]
        return x
    
    def same(self,x,y):
        return self.root(x) == self.root(y)
    
    def union(self,x,y):
        if not self.same(x,y):
            self.break_sum -= 2 * self.S[self.root(x)] * self.S[self.root(y)]
            #グループxとグループyが双方向に行き来可能になる
            if self.depth(x) < self.depth(y):
                self.S[self.root(y)] += self.S[self.root(x)]
                self.P[self.root(x)] = self.root(y)
            else:
                self.S[self.root(x)] += self.S[self.root(y)]
                self.P[self.root(y)] = self.root(x)

def solve(AB,n,m):
    #方針：全部の橋が壊れたところから橋を修復しながら逆算する
    Ans = []
    uf = UF(n)
    for i in range(m):
        Ans.append(uf.break_sum // 2)
        [a,b] = AB.pop()
        uf.union(a,b)
    for i in range(m//2):
        Ans[i],Ans[m-i-1] = Ans[m-i-1],Ans[i]
    return Ans

def main():
    n,m = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(m)]
    Ans = solve(AB,n,m)
    for i in range(m):
        print(Ans[i])

if __name__ == "__main__":
    main()
