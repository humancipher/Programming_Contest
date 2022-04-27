class UnionFind:
    def __init__(self,h,w):
        self.P = [i for i in range(h*w)]
    def depth(self,node):
        cnt = 0
        while self.P[node] != node:
            node = self.P[node]
            cnt += 1
        return cnt
    def root(self,node):
        while self.P[node] != node:
            node = self.P[node]
        return node
    def same(self,a,b):
        return self.root(a) == self.root(b)
    def union(self,a,b):
        if not self.same(a,b):
            if self.depth(a) > self.depth(b):
                self.P[self.root(b)] = self.P[self.root(a)]
            else:
                self.P[self.root(a)] = self.P[self.root(b)]

def main():
    h,w = map(int,input().split())
    Colored = [[False for _ in range(w)] for _ in range(h)]
    uf = UnionFind(h,w)
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    q = int(input())
    for _ in range(q):
        Que = list(map(int,input().split()))
        if Que[0] == 1:
            r,c = Que[1]-1,Que[2]-1
            Colored[r][c] = True
            for vx,vy in V:
                if 0 <= r+vx < h and 0 <= c+vy < w:
                    if Colored[r+vx][c+vy]:
                        uf.union(r*w+c,(r+vx)*w+(c+vy))
        else:
            ra,ca,rb,cb = Que[1]-1,Que[2]-1,Que[3]-1,Que[4]-1
            if Colored[ra][ca] and Colored[rb][cb]:
                if uf.same(ra*w+ca,rb*w+cb):
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")

if __name__ == "__main__":
    main()
