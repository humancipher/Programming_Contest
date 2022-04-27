N = 100
A = [i+1 for i in range(N)]

ans = 0
for i in range(N):
    ans += A[i] * (sum(A[0:i])+sum(A[i+1:N]))

print(ans)
