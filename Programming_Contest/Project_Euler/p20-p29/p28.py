N = 1001
n = (N+1)//2

A = [(2*i+1)**2 for i in range(n)]

ans = 1
for i in range(1,n):
    ans += ((A[i] + A[i] - 6*i) * 2)

print(ans)
