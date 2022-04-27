from bisect import bisect_left

n,q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
for _ in range(q):
    x = int(input())
    if A[0] >= x:
        print(n)
    else:
        print(n-bisect_left(A,x))
