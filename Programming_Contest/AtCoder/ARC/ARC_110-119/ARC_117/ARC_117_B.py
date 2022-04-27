N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

A.append(0)
A.sort()
ans = 1
for i in range(1,N+1):
    ans *= A[i] - A[i-1] + 1
    ans %= mod
print(ans)
