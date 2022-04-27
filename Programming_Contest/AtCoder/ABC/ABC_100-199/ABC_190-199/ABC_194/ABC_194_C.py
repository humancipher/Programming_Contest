N = int(input())
A = list(map(int,input().split()))

ans = 0
S = sum(A)
for i in range(N):
    ans += (N-1)*A[i]**2
    S -= A[i]
    ans -= 2*A[i]*S
print(ans)
