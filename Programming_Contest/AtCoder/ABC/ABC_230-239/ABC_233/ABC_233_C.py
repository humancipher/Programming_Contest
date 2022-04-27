n,x = map(int,input().split())
Mold = dict()
Mold[1] = 1
for _ in range(n):
    M = dict()
    LA = list(map(int,input().split()))
    for m in Mold:
        for i in range(1,len(LA)):
            if m * LA[i] in M:
                M[m*LA[i]] += Mold[m]
            elif m * LA[i] <= x:
                M[m*LA[i]] = Mold[m]
    Mold = M
if x in M:
    print(M[x])
else:
    print(0)
