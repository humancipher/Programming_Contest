n = int(input())
G = [list() for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
mx = 0
for i in range(1,n+1):
    mx = max(mx,len(G[i]))
if mx == n-1:
    print("Yes")
else:
    print("No")
