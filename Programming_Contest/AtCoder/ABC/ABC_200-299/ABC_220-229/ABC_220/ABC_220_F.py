from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10**6)

def Size(T,n,now,par):
    #S[i]に頂点i以下の部分木の大きさを書き込む
    ans = 1
    for nxt in T[now]:
        if nxt != par: #親ノードだけは外さないと親ノードに戻って無限ループになる
            ans += Size(T,n,nxt,now)
    S[now] = ans
    return ans

n = int(input())
T = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    T[u-1].append(v-1)
    T[v-1].append(u-1)

S = [-1] * n #S[i]:頂点i以下の部分木の大きさ
Size(T,n,0,-1)

D = [-1] * n #D[i]:頂点1から頂点iの距離
Ans = [-1] * n
Ans[0] = 0
Q = deque()
Q.append(0)
D[0] = 0
while len(Q) > 0:
    now = Q.popleft()
    for nxt in T[now]:
        if D[nxt] == -1:
            D[nxt] = D[now] + 1
            Ans[0] += D[nxt]
            Q.append(nxt)

Q = deque()
Q.append(0)
while len(Q) > 0:
    now = Q.popleft()
    for nxt in T[now]:
        if Ans[nxt] == -1:
            Ans[nxt] = Ans[now] + n - 2 * S[nxt]
            Q.append(nxt)
for i in range(n):
    print(Ans[i])
