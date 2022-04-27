INF = 10**10

def union(G,x):
    if len(G) == 0:
        return INF
    else:
        return 10*(len(G)-1) + abs(sum(G)-x)

n,a,b,c = map(int,input().split())
ABC = [a,b,c]
L = [int(input()) for _ in range(n)]

ans = INF
for i in range(4**n):
    G = [list() for _ in range(4)]
    x = i
    for j in range(n):
        G[x % 4].append(L[j])
        x //= 4
    tmp = 0
    for k in range(3):
        tmp += union(G[k],ABC[k])
    ans = min(ans,tmp)
print(ans)
