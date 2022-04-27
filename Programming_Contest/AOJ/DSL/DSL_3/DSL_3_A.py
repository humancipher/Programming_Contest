from bisect import bisect_left

n,s = map(int,input().split())
A = list(map(int,input().split()))
A = [0] + A
for i in range(1,n):
    A[i+1] += A[i]
ans = n+1
for i in range(n):
    if A[-1] - A[i] >= s:
        ans = min(ans,bisect_left(A,s+A[i])-i)
if ans == n+1:
    print(0)
else:
    print(ans)
