h,w,c,q = map(int,input().split())
TNC = [list(map(int,input().split())) for _ in range(q)]
D1,D2 = set(),set()
C = [0] * c
for _ in range(q):
    t,n,ci = TNC.pop()
    if t == 1:
        if n-1 not in D1:
            C[ci-1] += w - len(D2)
            D1.add(n-1)
    else:
        if n-1 not in D2:
            C[ci-1] += h - len(D1)
            D2.add(n-1)

print(" ".join(map(str,C)))