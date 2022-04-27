N,K,S = map(int,input().split())
INF = 10**9

A = []
for i in range(K):
    A.append(S)
if S != INF:
    for i in range(N-K):
        A.append(INF)
else:
    for i in range(N-K):
        A.append(INF-1)

print(" ".join(map(str,A)))
