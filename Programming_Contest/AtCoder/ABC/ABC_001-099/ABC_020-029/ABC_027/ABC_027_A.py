A = list(map(int,input().split()))

A.sort()

if A[0] == A[1]:
    print(A[2])
else:
    print(A[0])
