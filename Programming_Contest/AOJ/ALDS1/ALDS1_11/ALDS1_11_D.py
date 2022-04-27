n,m = map(int,input().split())
Rel = [tuple(map(int,input().split())) for _ in range(m)]
q = int(input())
Que = [tuple(map(int,input().split())) for _ in range(q)]

class UF:
    def __init__(self):
        self.roots = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def same(self,a,b):
        if self.find(a) == self.find(b):
            return True
        else:
            return False

    def find(self,a):
        if self.roots[a] == a:
            return a
        else:
            self.roots[a] = self.find(self.roots[a])
            return self.roots[a]

    def union(self,a,b):
        a,b = self.find(a),self.find(b)
        if a != b:
            if self.rank[a] >= self.rank[b]:
                self.roots[b] = a
                if self.rank[a] == self.rank[b]:
                    self.rank[b] += 1
            else:
                self.roots[a] = b

uf = UF()

for i in range(m):
    uf.union(Rel[i][0],Rel[i][1])

for i in range(q):
    if uf.same(Que[i][0],Que[i][1]):
        print("yes")
    else:
        print("no")
