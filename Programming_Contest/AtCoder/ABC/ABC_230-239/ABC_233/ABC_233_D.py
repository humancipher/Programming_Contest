n,k = map(int,input().split())
A = list(map(int,input().split()))
A = [0] + A
for i in range(n):
    A[i+1] += A[i]
M = dict()
ans = 0
for i in range(n+1):
    if A[i]-k in M:
        ans += M[A[i]-k]
    if A[i] in M:
        M[A[i]] += 1
    else:
        M[A[i]] = 1
print(ans)