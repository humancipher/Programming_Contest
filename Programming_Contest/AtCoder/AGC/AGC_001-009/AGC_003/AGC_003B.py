n = int(input())
A = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1):
    ans += A[i]//2
    A[i] %= 2
    if A[i] > 0 and A[i+1] > 0:
        ans += 1
        A[i] = 0
        A[i+1] -= 1
ans += A[n-1]//2
print(ans)