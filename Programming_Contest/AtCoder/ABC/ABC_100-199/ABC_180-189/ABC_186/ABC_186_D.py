N = int(input())
A = list(map(int,input().split()))
A.sort()

B = [A[i] for i in range(N)]

for i in range(N-1):
    B[i+1] += B[i]

ans = 0
for i in range(N-1):
    ans += (B[N-1] - B[i]) - A[i] * (N - 1 - i)
print(ans)
