N,M = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
C = set()
for a in A:
    if a not in B:
        C.add(a)
for b in B:
    if b not in A:
        C.add(b)
C = list(C)
C.sort()
print(" ".join(map(str,C)))
