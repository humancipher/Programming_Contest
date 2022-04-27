class Graph:
    def __init__(self,V,E):
        self.V = V
        #V[i]:頂点iの色
        self.E = E
        #E[i]:頂点iに隣接する頂点の集合

    def operate(self,s):
        if s[0] == 1:
            x = s[1]
            print(self.V[x])
            for v in self.E[x]:
                self.V[v] = self.V[x]
        else:
            x,y = s[1],s[2]
            print(self.V[x])
            self.V[x] = y

def main():
    N,M,Q = map(int,input().split())
    uv = [list(map(int,input().split())) for _ in range(M)]
    c = list(map(int,input().split()))
    s = [list(map(int,input().split())) for _ in range(Q)]

    c = [-1] + c
    E = [set() for _ in range(N+1)]
    for i in range(M):
        u,v = uv[i][0],uv[i][1]
        E[u].add(v)
        E[v].add(u)

    G = Graph(c,E)

    for i in range(Q):
        G.operate(s[i])

if __name__ == "__main__":
    main()
