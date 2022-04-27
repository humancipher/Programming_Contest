n = int(input())
L,R = [],[]
for _ in range(n):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

ans = 0
for i in range(n):
    eij = 0
    for j in range(i+1,n):
        for k in range(L[j],R[j]+1):
            if k < L[i]:
                eij += R[i]-L[i]+1
            else:
                eij += max(0,R[i]-k)
        eij /= ((R[i]-L[i]+1) * (R[j]-L[j]+1))
        ans += eij
        eij = 0
print(ans)
