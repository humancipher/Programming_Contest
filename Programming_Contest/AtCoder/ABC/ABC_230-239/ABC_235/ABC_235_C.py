n,q = map(int,input().split())
A = list(map(int,input().split()))
D = dict()
for i in range(n):
    if A[i] not in D:
        D[A[i]] = list()
    D[A[i]].append(i+1)
Ans = list()
for _ in range(q):
    x,k = map(int,input().split())
    if x in D:
        if len(D[x]) >= k:
            Ans.append(D[x][k-1])
        else:
            Ans.append(-1)
    else:
        Ans.append(-1)
for i in range(q):
    print(Ans[i])