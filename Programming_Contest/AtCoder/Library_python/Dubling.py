from collections import deque

#ダブリングで木の最近共通祖先を求める
class Dubling:
    def __init__(self,G,n,root,bitlen):
        self.G = G
        self.n = n
        self.root = root
        self.bitlen = bitlen
        self.Depth = [None] * n
        self.Depth[root] = 0
        self.D = [[None] * bitlen for _ in range(n)]
    def dubling(self):
        Q = deque()
        Q.append([self.root,-1])
        #D[i][j]:頂点iの2**j先の頂点
        while len(Q) > 0:
            now,par = Q.popleft()
            for nxt in self.G[now]:
                if nxt != par:
                    self.Depth[nxt] = self.Depth[now] + 1
                    self.D[nxt][0] = now
                    pt = 0
                    while pt+1 < self.bitlen and self.D[nxt][pt] != None:
                        self.D[nxt][pt+1] = self.D[self.D[nxt][pt]][pt]
                        pt += 1
                    Q.append([nxt,now])
    def ancestor(self,node,diff): #頂点nodeのdiff先の頂点
        if self.Depth[node] < diff:
            return None
        else:
            for j in range(self.bitlen):
                if 2**j & diff:
                    node = self.D[node][j]
                    diff -= 2**j
            return node
    def lca(self,x,y): #頂点xとyの最近共通祖先
        if self.Depth[x] < self.Depth[y]:
            y = self.ancestor(y,self.Depth[y] - self.Depth[x])
        elif self.Depth[x] > self.Depth[y]:
            x = self.ancestor(x,self.Depth[x] - self.Depth[y])
        left,right = -1,self.n
        while right - left > 1:
            mid = (left+right)//2
            if self.ancestor(x,mid) == self.ancestor(y,mid):
                right = mid
            else:
                left = mid
        return self.ancestor(x,right)