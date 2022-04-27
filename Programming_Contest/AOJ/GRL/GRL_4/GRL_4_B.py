def dfs(G,v):
    if Use[v]:
        for c in G[v]:
            dfs(G,c)
        Use[v] = False
        A.append(v)

def TPS(G,n):
    for i in range(n):
       if Use[i]:
           dfs(G,i)
    for i in range(len(A)//2):
        A[i],A[-1-i] = A[-1-i],A[i]
    return A

V,E = map(int,input().split())
G = [set() for _ in range(V)]
for _ in range(E):
    s,t = map(int,input().split())
    G[s].add(t)
A = []
Use = [True for _ in range(V)]
tps = TPS(G,V)
for i in range(V):
    print(tps[i])
