n,k,x = map(int,input().split())
A = list(map(int,input().split()))
for i in range(n):
    d = min(k,A[i]//x)
    A[i] -= d*x
    k -= d
if k == 0:
    print(sum(A))
else:
    A.sort(reverse=True)
    if k > n:
        print(0)
    else:
        for i in range(k):
            A[i] = 0
        print(sum(A))